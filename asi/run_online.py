import os
import json
import argparse
import subprocess
from subprocess import Popen
import random
import datetime
import shutil
from tqdm import tqdm

def parse_task_ids(task_id_str: str) -> list[str]:
    random.seed(args.seed)
    chunks = [c.strip() for c in task_id_str.split(",")]
    task_id_list = []
    for c in chunks:
        chunk = c.split("-")
        if len(chunk) == 1:
            s, e = int(chunk[0]), int(chunk[0])
        else:
            s, e = int(chunk[0].strip()), int(chunk[1].strip())
        # s, e = [int(n.strip()) for n in c.split("-")]
        task_id_list.extend([str(i) for i in range(s, e+1)])
    random.shuffle(task_id_list)
    return task_id_list

def filter_by_website(task_id_list: list[str], website: str) -> list[str]:
    filtered_task_id_list = []
    for tid in task_id_list:
        config_path = f"config_files/{tid}.json"
        if not os.path.exists(config_path):
            print(f"Config file {config_path} does not exist.")
            continue
        else:
            config = json.load(open(config_path, 'r'))
            if config["sites"] != [website]:
                print(f"Config file {config_path} does not match the website {website}.")
                continue
            else:
                filtered_task_id_list.append(tid)
    return filtered_task_id_list

# %% Baseline

def run_vanilla():
    task_id_list = parse_task_ids(args.task_ids)

    for tid in task_id_list:
        # step 1: task solving
        process = Popen([
            "python", "run_demo.py",
            "--task_name", f"webarena.{tid}",
            "--headless",
            "--model_name", args.model,
        ])
        try:
            stdout, stderr = process.communicate(timeout=200)
            print(stdout)
        except subprocess.TimeoutExpired as e:
            process.kill()
            stdout, stderr = process.communicate() # Clean up resources
            print(f"Process timed out after {e.timeout} seconds.")
            print(stderr)

# %% AWM

def run_awm():
    task_id_list = parse_task_ids(args.task_ids)

    for tid in task_id_list:
        # step 1: task solving
        process = Popen([
            "python", "run_demo.py",
            "--task_name", f"webarena.{tid}",
            "--memory_path", f"workflows/{args.website}.txt",
            "--headless",
            "--model_name", args.model,
            "--use_screenshot", "True",
            "--max_steps", "30",
        ])
        process.wait()
        # input("[1] Completed task solving")

        # step 2: eval traj
        process = Popen([
            "python", "-m", "autoeval.evaluate_trajectory",
            "--result_dir", f"results/webarena.{tid}",
        ])
        process.wait()
        path = f"results/webarena.{tid}/gpt-4o-2024-05-13_autoeval.json"
        if os.path.exists(path):
            is_correct = json.load(open(path))[0]["rm"]  # bool
        else:
            is_correct = False
        if not is_correct: continue
        # input("[2] Completed evaluated trajectory (true)")

        # step 3: induce workflows
        process = Popen([
            "python", "-m", "results.calc_valid_steps",
            "--clean_and_store", "--result_dir", f"results/webarena.{tid}",
            "--model", f"{args.model}",
        ])
        process.wait()  # output 'clean_steps.json'
        # input("[3.1] Completed clean trajectory")

        process = Popen([
            "python", "-m", "induce.induce_memory",
            "--website", args.website,
            "--result_id_list", tid,
        ])
        process.wait()  # write to 'workflows/{args.website}.txt'
        # input("[3.2] Completed induced workflow")

        # intermediate supervision
        # cont = input("Continue? (y/n)")

# %% ASI
def run_asi():
    task_id_list = parse_task_ids(args.task_ids)
    print(f"Total task ids: {len(task_id_list)}")
    task_id_list = filter_by_website(task_id_list, args.websites)
    print(f"Filtered task ids: {len(task_id_list)}")
    
    
    for i, tid in tqdm(enumerate(task_id_list), desc="Processing tasks", total=len(task_id_list)):
        if (i + 1) % args.save_interval == 0:
            # Create backup directory if it doesn't exist
            backup_dir = f"actions/backups"
            os.makedirs(backup_dir, exist_ok=True)
            
            # Create timestamped backup of the actions file
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"{args.websites}_step_{i+1}_{timestamp}.py"
            backup_path = os.path.join(backup_dir, backup_filename)
            
            # Copy the current actions file to backup
            actions_file = f"actions/{args.websites}.py"
            if os.path.exists(actions_file):
                shutil.copy2(actions_file, backup_path)
                print(f"Saved induced actions backup to {backup_path} after {i+1} processed tasks")
            else:
                print(f"Warning: Actions file {actions_file} not found for backup")

        # step 1: task solving
        process = Popen([
            "python", "run_demo.py",
            "--task_name", f"webarena.{tid}",
            "--websites", args.websites,
            "--headless",
            "--model_name", args.model,
            "--use_screenshot", "True",
            "--max_steps", "30",
        ])
        try:
            stdout, stderr = process.communicate(timeout=300)
            print("Process completed successfully:")
            print(stdout)
        except subprocess.TimeoutExpired as e:
            process.kill()
            stdout, stderr = process.communicate() # Clean up resources
            print(f"Process timed out after {e.timeout} seconds.")
            print(stderr)
            continue
        # input("[1] Completed task solving")
        path = f"results/webarena.{tid}/summary_info.json"
        if json.load(open(path, 'r'))["n_steps"] < 3: continue

        # step 2: eval traj
        process = Popen([
            "python", "-m", "autoeval.evaluate_trajectory",
            "--result_dir", f"results/webarena.{tid}",
            "--model", f"{args.model}",
        ])
        model_name = args.model.replace("/", "_")
        process.wait()
        path = f"results/webarena.{tid}/{model_name}_autoeval.json"
        try:
            is_correct = json.load(open(path))[0]["rm"]  # bool
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            is_correct = False
        if not is_correct: continue
        # input("[2.1] Completed evaluated trajectory (true)")
        process = Popen([
            "python", "-m", "results.calc_valid_steps",
            "--clean_and_store", "--result_dir", f"results/webarena.{tid}",
            "--model", f"{args.model}",
        ])
        process.wait()  # output 'clean_steps.json'
        # input("[2.2] Completed clean trajectory")

        # step 3: induce actions
        process = Popen([
            "python", "-m", "induce.induce_actions",
            "--website", args.websites,
            "--result_id_list", tid,
            "--model", f"{args.model}",
        ])
        try:
            stdout, stderr = process.communicate(timeout=200)
            print(stdout)
        except subprocess.TimeoutExpired as e:
            process.kill()
            stdout, stderr = process.communicate() # Clean up resources
            print(f"Process timed out after {e.timeout} seconds.")
            print(stderr)
        # input("[3] Completed induced workflow")
    

        # intermediate supervision
        # cont = input("Continue? (y/n)")

# %% Verified, Program
def run_veri_program():
    task_id_list = parse_task_ids(args.task_ids)
    
    # Initialize counter for processed tasks
    processed_tasks = 0
    
    for tid in task_id_list:
        # step 1: task solving with memory input
        process = Popen([
            "python", "run_demo.py", "--headless",
            "--task_name", f"webarena.{tid}",
            "--memory_path", f"workflows/{args.website}.txt",
        ])
        try:
            stdout, stderr = process.communicate(timeout=300)
            print("Process completed successfully:")
            print(stdout)
        except subprocess.TimeoutExpired as e:
            process.kill()
            stdout, stderr = process.communicate() # Clean up resources
            print(f"Process timed out after {e.timeout} seconds.")
            print(stderr)
            continue
        # input("[1] Completed task solving")
        path = f"results/webarena.{tid}/summary_info.json"
        if json.load(open(path, 'r'))["n_steps"] < 3: continue

        # step 2: eval traj
        process = Popen([
            "python", "-m", "autoeval.evaluate_trajectory",
            "--result_dir", f"results/webarena.{tid}",
        ])
        process.wait()
        path = f"results/webarena.{tid}/gpt-4o-2024-05-13_autoeval.json"
        is_correct = json.load(open(path))[0]["rm"]  # bool
        if not is_correct: continue
        # input("[2.1] Completed evaluated trajectory (true)")
        process = Popen([
            "python", "-m", "results.calc_valid_steps",
            "--clean_and_store", "--result_dir", f"results/webarena.{tid}",
            "--model", f"{args.model}",
        ])
        process.wait()  # output 'clean_steps.json'
        # input("[2.2] Completed clean trajectory")

        # step 3: induce actions
        orignal_content = open(f"actions/{args.website}.py", 'r').read()
        process = Popen([
            "python", "-m", "induce.induce_actions",
            "--website", args.website,
            "--result_id_list", tid,
        ])
        try:
            stdout, stderr = process.communicate(timeout=200)
            print(stdout)
        except subprocess.TimeoutExpired as e:
            process.kill()
            stdout, stderr = process.communicate() # Clean up resources
            print(f"Process timed out after {e.timeout} seconds.")
            print(stderr)
            continue
        updated_content = open(f"actions/{args.website}.py", 'r').read()
        if orignal_content != updated_content:
            new_content = updated_content[len(orignal_content):].strip()
            with open(f"workflows/{args.website}.txt", 'a') as f:
                f.write(new_content + "\n\n")
        # input("[3] Completed induced workflow")

        # Increment counter for successfully processed tasks
        processed_tasks += 1
        
        # Save induced actions every save_interval steps
        if processed_tasks % args.save_interval == 0:
            # Create backup directory if it doesn't exist
            backup_dir = f"actions/backups"
            os.makedirs(backup_dir, exist_ok=True)
            
            # Create timestamped backup of the actions file
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"{args.website}_step_{processed_tasks}_{timestamp}.py"
            backup_path = os.path.join(backup_dir, backup_filename)
            
            # Copy the current actions file to backup
            actions_file = f"actions/{args.website}.py"
            if os.path.exists(actions_file):
                shutil.copy2(actions_file, backup_path)
                print(f"Saved induced actions backup to {backup_path} after {processed_tasks} processed tasks")
            else:
                print(f"Warning: Actions file {actions_file} not found for backup")

        # intermediate supervision
        # cont = input("Continue? (y/n)")

# %% Memory-Augmented ASI

def run_mem_asi():
    task_id_list = parse_task_ids(args.task_ids)
    for tid in task_id_list:
        # step 1: task solving
        process = Popen([
            "python", "run_demo.py",
            "--task_name", f"webarena.{tid}",
            "--websites", args.website,
            "--headless"
        ])
        try:
            stdout, stderr = process.communicate(timeout=300)
            print("Process completed successfully:")
            print(stdout)
        except subprocess.TimeoutExpired as e:
            process.kill()
            stdout, stderr = process.communicate() # Clean up resources
            print(f"Process timed out after {e.timeout} seconds.")
            print(stderr)
            continue
        # input("[1] Completed task solving")
        path = f"results/webarena.{tid}/summary_info.json"
        if json.load(open(path, 'r'))["n_steps"] < 3: continue

        # step 2: eval traj
        process = Popen([
            "python", "-m", "autoeval.evaluate_trajectory",
            "--result_dir", f"results/webarena.{tid}",
        ])
        process.wait()
        path = f"results/webarena.{tid}/gpt-4o-2024-05-13_autoeval.json"
        is_correct = json.load(open(path))[0]["rm"]  # bool
        if not is_correct: continue
        # input("[2.1] Completed evaluated trajectory (true)")
        process = Popen([
            "python", "-m", "results.calc_valid_steps",
            "--clean_and_store", "--result_dir", f"results/webarena.{tid}",
        ])
        process.wait()  # output 'clean_steps.json'
        # input("[2.2] Completed clean trajectory")

        # step 3: induce actions
        nlines = len(open(f"actions/{args.website}.py", 'r').readlines())
        process = Popen([
            "python", "-m", "induce.induce_actions",
            "--website", args.website,
            "--result_id_list", tid,
        ])
        try:
            stdout, stderr = process.communicate(timeout=300)
            print("Process completed successfully:")
            print(stdout)
        except subprocess.TimeoutExpired as e:
            process.kill()
            stdout, stderr = process.communicate() # Clean up resources
            print(f"Process timed out after {e.timeout} seconds.")
            print(stderr)
            continue
        input("[3] Completed induced actions")

        # step 4: induce memory
        new_nlines = len(open(f"actions/{args.website}.py", 'r').readlines())
        if new_nlines == nlines: continue
        if new_nlines == nlines: task_abbr = tid
        else: task_abbr = f"{tid}_test"

        output_path = f"results/webarena.{task_abbr}/cleaned_steps.json"
        if not os.path.exists(output_path):
            process = Popen([
                "python", "-m", "results.calc_valid_steps",
                "--clean_and_store",
                "--result_dir", f"results/webarena.{task_abbr}",
                "--model", f"{args.model}",
            ])
            process.wait()  # output 'clean_steps.json'
            # input("[4.1] Completed clean trajectory")
        process = Popen([
            "python", "-m", "induce.induce_memory",
            "--website", args.website,
            "--result_id_list", task_abbr,
            "--model", f"{args.model}",
        ])
        process.wait()
        input("[4.2] Completed induce memory")

        # intermediate supervision
        cont = input("Continue? (y/n)")

# %% Action only demo

def run_asi_vanilla():
    task_id_list = parse_task_ids(args.task_ids)
    print(f"Total task ids: {len(task_id_list)}")
    task_id_list = filter_by_website(task_id_list, args.websites)
    print(f"Filtered task ids: {len(task_id_list)}")
    
    for tid in tqdm(task_id_list, desc="Processing tasks", total=len(task_id_list)):
        process = Popen([
            "python", "run_demo.py",
            "--task_name", f"webarena.{tid}",
            "--websites", args.websites,
            "--headless",
            "--model_name", args.model,
            "--use_screenshot", "True",
            "--max_steps", "20",
            "--output_dir", "results_asi_vanilla_gpt-4o",
        ])
        try:
            stdout, stderr = process.communicate(timeout=300)
            print("Process completed successfully:")
            print(stdout)
        except subprocess.TimeoutExpired as e:
            process.kill()
            stdout, stderr = process.communicate() # Clean up resources
            print(f"Process timed out after {e.timeout} seconds.")
            continue
# %% Main Pipeline

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment", type=str, required=True,
                        choices=["vanilla", "awm", "asi", "mem_asi", "veri_program", "veri_text", "asi_vanilla"])
    parser.add_argument("--websites", type=str, required=True,
                        choices=["shopping", "admin", "reddit", "gitlab", "map"])
    parser.add_argument("--task_ids", type=str, required=True,
                        help="xxx-xxx,xxx-xxx")
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--save_interval", type=int, default=10)
    
    args = parser.parse_args()

    if args.experiment == "vanilla":
        run_vanilla()
    elif args.experiment == "awm":
        run_awm()
    elif args.experiment == "asi":
        run_asi()
    elif args.experiment == "mem_asi":
        run_mem_asi()
    elif args.experiment == "asi_vanilla":
        run_asi_vanilla()
