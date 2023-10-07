import re
import replicate
import openai
from selfmodifai.agents.open_source_agent.replace_code import replace_code


def open_source_agent():
    codellama_model_version = (
        "meta/codellama-34b-instruct:8281a5c610f6e88237ff3ddaf3c33b56f60809e2bdd19fbec2fda742aa18167e"
    )
    llama2_model_version = "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3"

    with open("prompts/nanogpt/researcher.txt", "r") as f:
        prompt = f.read()
    output = replicate.run(
        codellama_model_version,
        input={
            "prompt": prompt,
            "max_tokens": 5000,
            # "temperature": 0.76,
        },
    )
    # The meta/codellama-34b-instruct model can stream output as it's running.
    # The predict method returns an iterator, and you can iterate over that output.
    # output_list = list(output)
    # print(output_list)
    output_str = "".join(output)

    print("Llama 2:\n", output_str)

    # training_file_path = "/selfmodifai/selfmodifai-gpt-dev/gpt_dev/train.py"
    training_file_path = "gpt-dev/train.py"

    with open(training_file_path, "r") as f:
        training_file = f.read()

    engineer_prompt = (
        "This is my training script:\n" + training_file + "\n\nCan you add these changes to it:\n" + output_str
    )
    gpt_api_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": engineer_prompt},
    ]
    engineer_response = openai.ChatCompletion.create(model="gpt-4", messages=gpt_api_messages)
    engineer_response_content = engineer_response["choices"][0]["message"]["content"]

    print("GPT-4:\n", engineer_response_content)

    pattern = r"```python\n(.*?)\n```"
    er_search = re.search(pattern, engineer_response_content, re.DOTALL)
    if er_search:
        er_code = er_search.group(1)
        replace_code(er_code)
