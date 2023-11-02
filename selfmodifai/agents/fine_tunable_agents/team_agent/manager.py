import openai
import json

# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def detect_list_approaches(list_exists):
    return list_exists


def run_conversation():
    # Step 1: send the conversation and available functions to GPT
    messages = [{"role": "user", "content": "Are there a list of approaches in this text:"}]
    functions = [
        {
            "name": "detect_list_approaches",
            "description": "Detect if the text contains a list of approaches",
            "parameters": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "bool",
                        "description": "Whether this is a list of approaches",
                    },
                    "unit": {"type": "bool", "enum": [True, False]},
                },
                "required": ["list"],
            },
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]

    # Step 2: check if GPT wanted to call a function
    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "detect_list_approaches": detect_list_approaches,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        function_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = function_to_call(
            location=function_args.get("location"),
            unit=function_args.get("unit"),
        )
        print(function_response)
