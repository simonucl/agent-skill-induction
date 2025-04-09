# %% Action
ACTIONS = ["click", "fill", "keyboard_press", "scroll", "send_msg_to_user", "observe", "hover", "select_option"]

def extract_code_pieces(
    text: str, 
    start: str = "```", end: str = "```",
    do_split: bool = True,
) -> list[str]:
    """Extract code pieces from a text string.
    Args:
        text: str, model prediciton text.
    Rets:
        code_pieces: list[str], code pieces in the text.
    """
    code_pieces = []
    while start in text:
        st_idx = text.index(start) + len(start)
        if end in text[st_idx:]:
            end_idx = text.index(end, st_idx)
        else: 
            end_idx = len(text)
        
        if do_split:
            code_pieces.extend(text[st_idx:end_idx].strip().split("\n"))
        else:
            code_pieces.append(text[st_idx:end_idx].strip())
        text = text[end_idx+len(end):].strip()
    return code_pieces


def is_action_valid(action: str) -> bool:
    """Check if the provided action is valid."""
    if "click(" in action:
        arg = action[action.index("(")+1: action.index(")")]
        return type(eval(arg)) == str
    elif "fill(" in action:
        arg = action[action.index("(")+1: action.index(",")].strip()
        return type(eval(arg)) == str
    else:
        return True


# %% Task
import os
import json

def if_add_result(result_dir: str) -> bool:
    """Decide if to add the result to the induction input list."""
    autoeval_path = os.path.join(result_dir, "gpt-4o_autoeval.json")
    if os.path.exists(autoeval_path) and json.load(open(autoeval_path))[0]["rm"] != True:
            return False
    else:
        summary_path = os.path.join(result_dir, "summary_info.json")
        if (not os.path.exists(summary_path)) or (json.load(open(summary_path))["cum_reward"] != 1.0):
            return False
    return True


def get_result_dirs(
    results_dir: str, result_id_list: list[str] = None, 
    template_id: str = None, config_dir: str = None,
) -> str:
    if template_id is None:
        if result_id_list is None: # add all webarena.* under `results_dir`
            result_dir_list = [os.path.join(results_dir) for d in os.listdir(results_dir) if d.startswith("webarena.")]
        else:
            result_dir_list = [f"webarena.{rid}" for rid in result_id_list]
            result_dir_list = [rd for rd in result_dir_list if rd in os.listdir(results_dir)]
            result_dir_list = [os.path.join(results_dir, rd) for rd in result_dir_list]
    else: # find config files of template_id
        config_files = sorted(os.listdir(config_dir), key=lambda x: int(x.split('.')[0]))
        config_ids = [
            f.split('.')[0] for f in config_files 
            if json.load(open(os.path.join(config_dir, f)))["intent_template_id"] == int(template_id)
        ]
        result_dir_list = []
        for cid in config_ids:
            rdir = os.path.join(results_dir, f"webarena.{cid}")
            if if_add_result(rdir):
                result_dir_list.append(rdir)
        # if len(result_dir_list) < 1: return []
        print("No Template ID: ", result_dir_list)
    return result_dir_list


def get_task_id(result_dir: str) -> str:
    task_name = result_dir.split('/')[-1]
    task_id = task_name.split('.')[1]
    if '_' in task_id:
        task_id = task_id.split('_')[0]
    return task_id


# %% Query

def get_thoughts_and_actions(block: list[str], prefix: str = "browsergym.experiments.loop - INFO - action:") -> dict:
    """Extract thoughts and actions from a step block."""
    text = ''.join(block)
    if prefix not in text: return {"thought": "", "action": []}
    sidx = text.index(prefix) + len(prefix)
    if "```" not in text[sidx:]: eidx = len(text)
    else: eidx = text.index("```", sidx)
    thought = text[sidx: eidx].replace("\n\n", "\n").strip()
    step = {"thought": thought, "action": []}

    code_pieces = extract_code_pieces(text)
    
    for cp in code_pieces:
        if is_action_valid(cp.strip()):
            step["action"].append(cp.strip())
    
    return step


def extract_steps(path: str) -> list[dict]:
    """Process steps from the log file."""
    lines = open(path, 'r').readlines()
    blocks, curr_block = [], []
    for line in lines:
        if "browsergym.experiments.loop - INFO" in line:
            if curr_block:
                blocks.append(curr_block)
                curr_block = []
        curr_block.append(line)
    if curr_block:
        blocks.append(curr_block)

    steps = [get_thoughts_and_actions(block) for block in blocks]
    steps = [s for s in steps if len(s["action"]) > 0]
    return steps


def serialize_step(step: dict) -> str:
    lines = [f"{step['thought']}"]
    for action in step["action"]:
        lines.append(f"```{action}```")
    return '\n'.join(lines)


def get_example_query(index: int, result_dir: str, config_dir: str) -> str:
    """Get the string for a past example experience."""
    cid = get_task_id(result_dir)
    config_path = os.path.join(config_dir, f"{cid}.json")
    config = json.load(open(config_path))
    instruction = config["intent"]
    task = config["intent_template"]

    log_path = os.path.join(result_dir, "experiment.log")
    steps = extract_steps(log_path)
    steps = '\n'.join([serialize_step(s) for s in steps])

    return f"### Example {index} ({config['task_id']}): {instruction}\n{steps}", task


# %% Path

def get_output_dir(args, key: str = "action") -> str:
    """Get the output directory."""
    if args.template_id is not None:
        args.output_path = os.path.join("outputs", args.website, f"{args.template_id}.md")
        args.output_dir = os.path.join("outputs", args.website, f"{args.template_id}")
    else:
        args.output_dir = os.path.join(
            "outputs", args.website, f"{key}_task-{'-'.join(args.result_id_list)}"
        )
    return args


# %% Actions

import ast

def count_function_calls(function_code: str, threshold: int = 1):
    """
    Count the number of function calls in the given function implementation.

    Args:
        function_code (str): The code of the function as a string.
        threshold (int): The minimum number of function calls to return True.

    Returns:
        int: The number of function calls in the code.
    """
    # Parse the function code into an AST
    tree = ast.parse(function_code)
    
    # Find all nodes that are function calls
    function_calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)]
    
    # Return the number of function call nodes
    def_counts = function_code.count("def ")
    return len(function_calls) > (threshold * def_counts)


def get_function_names(function_code: str, existing_names: list[str] = []) -> list[str]:
    """Get the names of defined functions in the code."""
    tree = ast.parse(function_code)
    names = [
        fdef.name for fdef in tree.body 
        if isinstance(fdef, ast.FunctionDef)
    ]
    names = [n for n in names if n not in existing_names]
    return names


# %% Test

def clean_test(test: str, actions: set, add_action: bool = True) -> str:
    """Remove steps before or after the first call of induced action."""
    test_lines = test.split('\n')
    end_index = len(test_lines)
    for i, tl in enumerate(test_lines):
        if any([a in tl for a in actions]):
            end_index = i + int(add_action)
            break
    return '\n'.join([tl for tl in test_lines[: end_index] if not tl.startswith("# ") and tl.strip()])


def parse_tests(response: str, action_names: list[str]) -> list[str]:
    """Parse the list of tests from model response."""
    if "rewritten trajectories" in response.lower():
        index = response.lower().index("rewritten trajectories")
        response = response[index:].lstrip()
    tests = extract_code_pieces(response, start="```python", end="```", do_split=False)
    tests = [t for t in tests if "def " not in t]
    tests = [clean_test(t, action_names) for t in tests]
    return tests
