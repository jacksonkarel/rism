import re
import replicate
import openai


def open_source_agent():
    with open("prompts/nanogpt/researcher.txt", "r") as f:
        prompt = f.read()
    output = replicate.run(
        "meta/codellama-34b-instruct:8281a5c610f6e88237ff3ddaf3c33b56f60809e2bdd19fbec2fda742aa18167e",
        input={
            "prompt": prompt,
            "max_tokens": 5000,
        },
    )
    # The meta/codellama-34b-instruct model can stream output as it's running.
    # The predict method returns an iterator, and you can iterate over that output.
    # output_list = list(output)
    # print(output_list)
    output_str = "".join(output)

    # training_file_path = "/selfmodifai/selfmodifai-gpt-dev/gpt_dev/train.py"
    training_file_path = "../selfmodifai-gpt-dev/gpt_dev/train.py"

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
    pattern = r"```python\n(.*?)\n```"
    er_search = re.search(pattern, engineer_response_content, re.DOTALL)
    if er_search:
        er_code = er_search.group(1)
        with open(training_file_path, "w") as f:
            f.write(er_code)
            print(er_code)
