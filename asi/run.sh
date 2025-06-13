export BASE_URL=https://sa-homepage-aa-1.chats-lab-gui-agent.uk
export SUFFIX=aa-1
export DOMAIN_NAME=chats-lab-gui-agent.uk
export WA_HOMEPAGE="https://sa-homepage-${SUFFIX}.${DOMAIN_NAME}"
export WA_SHOPPING="https://sa-shopping-${SUFFIX}.${DOMAIN_NAME}/"
export WA_SHOPPING_ADMIN="https://sa-shopping-admin-${SUFFIX}.${DOMAIN_NAME}/admin"
export WA_REDDIT="https://sa-forum-${SUFFIX}.${DOMAIN_NAME}"
export WA_GITLAB="https://sa-gitlab-${SUFFIX}.${DOMAIN_NAME}"
export WA_FULL_RESET="https://sa-reset-${SUFFIX}.${DOMAIN_NAME}"
# Those are not functional sites but are emptily defined here for compatibility with browsergym
export WA_WIKIPEDIA="https://sa-wikipedia-${SUFFIX}.${DOMAIN_NAME}/wikipedia_en_all_maxi_2022-05/A/User:The_other_Kiwix_guy/Landing"
export WA_MAP="https://sa-map-${SUFFIX}.${DOMAIN_NAME}"

export PYTHONPATH="$PYTHONPATH:$(pwd)"
MODEL=anthropic/claude-sonnet-4-20250514
TASK_ID=21
RERUN=false
rm -rf outputs/*
python3 config_files/generate_test_data.py


 if [ "$RERUN" = true ]; then
    rm -rf results/webarena.*
    # Clean outputs directory if it exists
    python run_demo.py \
        --task_name "webarena.${TASK_ID}" \
        --websites "shopping" \
        --model_name ${MODEL} \
        --headless
fi

python autoeval/evaluate_trajectory.py \
    --result_dir "results/webarena.${TASK_ID}" \
    --model gpt-4o


python -m results.calc_valid_steps \
    --clean_and_store \
    --result_dir results/webarena.${TASK_ID} \
    --model ${MODEL}

python induce/induce_actions.py \
    --result_id_list ${TASK_ID} \
    --website "shopping" \
    --model ${MODEL}