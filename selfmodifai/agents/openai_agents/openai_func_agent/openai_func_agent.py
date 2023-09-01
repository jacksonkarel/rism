import openai
import json
from selfmodifai.agents.openai_agents.openai_manager import openai_manager
from selfmodifai.agents.openai_agents.helpers import update_messages
import os


# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)


def openai_func_agent():
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    messages_path = "./prompts/new_architecture.json"

    with open(messages_path) as json_file:
        messages = json.load(json_file)

    # Step 1: send the conversation and available functions to GPT

    while True:
        manager_sys_prompt = "You are keeping an AI language model that is trying to create a better model architecture than transformers on track."
        manager_response = openai_manager(messages)
        messages.append({"role": "assistant", "content": manager_response})

        response = openai.ChatCompletion.create(model="gpt-4", messages=messages)

        response_content = response["choices"][0]["message"]["content"]
        print(f"Researcher: {response_content}")

        messages = update_messages(response_content, "assistant", messages, messages_path)

    # functions = [
    #     {
    #         "name": "get_current_weather",
    #         "description": "Get the current weather in a given location",
    #         "parameters": {
    #             "type": "object",
    #             "properties": {
    #                 "location": {
    #                     "type": "string",
    #                     "description": "The city and state, e.g. San Francisco, CA",
    #                 },
    #                 "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
    #             },
    #             "required": ["location"],
    #         },
    #     }
    # ]
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo-0613",
    #     messages=messages,
    #     functions=functions,
    #     function_call="auto",  # auto is default, but we'll be explicit
    # )
    # response_message = response["choices"][0]["message"]

    # # Step 2: check if GPT wanted to call a function
    # if response_message.get("function_call"):
    #     # Step 3: call the function
    #     # Note: the JSON response may not always be valid; be sure to handle errors
    #     available_functions = {
    #         "get_current_weather": get_current_weather,
    #     }  # only one function in this example, but you can have multiple
    #     function_name = response_message["function_call"]["name"]
    #     fuction_to_call = available_functions[function_name]
    #     function_args = json.loads(response_message["function_call"]["arguments"])
    #     function_response = fuction_to_call(
    #         location=function_args.get("location"),
    #         unit=function_args.get("unit"),
    #     )

    #     # Step 4: send the info on the function call and function response to GPT
    #     messages.append(response_message)  # extend conversation with assistant's reply
    #     messages.append(
    #         {
    #             "role": "function",
    #             "name": function_name,
    #             "content": function_response,
    #         }
    #     )  # extend conversation with function response
    #     second_response = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo-0613",
    #         messages=messages,
    #     )  # get a new response from GPT where it can see the function response
    #     return second_response
