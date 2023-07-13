from selfmodifai.falcon_40b_agent.falcon_40b_generate import falcon_40b_generate


def falcon_40b_agent():
    base_prompt = f"""I am a highly intellgient AI agent that is improving the model architecture of the language model Alpaca-LoRA. I write bash commands that are then executed and the outputs are then returned to me. This helps me understand the Alpaca-LoRA codebase and improve the model architecture of Alpaca-LoRA.\n\nTo better understand the Alpaca-LoRA codebase, I should"""

    print(falcon_40b_generate(base_prompt))
