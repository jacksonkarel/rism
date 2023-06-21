import os
import re
import json
from transformers import pipeline
import openai
from openai.error import InvalidRequestError
from selfmodifai.handle_too_long_context import handle_too_long_context
from selfmodifai.helpers import update_messages, format_nbl, detect_non_bash_code

def gpt4_agent(messages_path):
    openai.api_key = os.environ("OPENAI_API_KEY")
    
    with open(messages_path) as json_file:
        messages = json.load(json_file)

    while True:

        try:
            response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
            )
        except InvalidRequestError as e:
            # Check if the error message matches the context length issue
            if "maximum context length" in str(e):
                response, messages = handle_too_long_context(messages)

                with open(messages_path, 'w') as outfile:
                    json.dump(messages, outfile)

            else:
                # Re-raise the exception if it's not what we're looking for
                raise e

        response_content = response["choices"][0]["message"]["content"]

        messages = update_messages(response_content, "assistant", messages, messages_path)

        # Define the regular expression pattern
        pattern = r'```bash\n(.*?)\n```'

        bash_matches = re.findall(pattern, response_content, re.DOTALL)

        non_bash_languages = detect_non_bash_code(response_content)

        bash_response = "Create bash commands that do that. Give me them one by one."
        if bash_matches:
            content = ""
        # matches is now a list of all bash commands in the string
            for bash_command in bash_matches:
                content += f"{bash_command}:\n"
                stream = os.popen(bash_command)

                content += stream.read()


            if non_bash_languages:
                nbl_str = format_nbl(non_bash_languages)

                content += f"Those are the outputs from those bash commands. Can you write bash commands to implement the {nbl_str} code?"

            elif not content:
                content = "Ok, did that"

        elif non_bash_languages:
            languages = format_nbl(non_bash_languages)
            content = f"Write bash commands to implement those changes in the {languages} files."

        elif "?" not in response_content:
            content = bash_response

        else:
            classifier = pipeline("zero-shot-classification")
            labels = ["suggestion for what to do next", "inquisitive question", "asking somebody to do something"]
            results = classifier(sequences=response_content, candidate_labels=labels, hypothesis_template="This text is a {}")

            if results["labels"][0] == "suggestion for what to do next":
                content = bash_response

            else:
                content = "My goal is to improve the model architecture of Alpaca-LoRA to make it a more powerful language model. Find the answer to that question in that context. If you can't, try another step in improving the language model."


        messages = update_messages(content, "user", messages, messages_path)