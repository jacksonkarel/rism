import re
import logging
from selfmodifai.helpers import openai_response, new_openai_mru
from selfmodifai.agents.fine_tunable_agents.team_agent.ta_engineer.ta_engineer import ta_engineer


def team_agent():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Create an artificial neural network architecture for text generation that no one has thought of yet that attempts to be very good at generalization",
        },
    ]
    brainstorm_response_content = openai_response("gpt-3.5-turbo-1106", messages, "Brainstorm")

    # Pattern to match code blocks
    pattern = r"```(\w+)\n(.*?)```"

    contains_code = re.search(pattern, brainstorm_response_content, re.DOTALL)

    if contains_code:
        logging.info("\nBrainstorm contains code")

    else:
        model_code, messages = ta_engineer(brainstorm_response_content, messages, pattern)

        train_on_dataset_prompt = "Train a model on text from the file brittancica.txt"
        train_on_data_ru = new_openai_mru("gpt-4", train_on_dataset_prompt, messages, "Train on dataset")
