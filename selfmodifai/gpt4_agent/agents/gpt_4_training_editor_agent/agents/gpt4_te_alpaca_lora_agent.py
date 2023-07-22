from selfmodifai.gpt4_agent.agents.gpt_4_training_editor_agent.gpt4_training_editor_agent import Gpt4TrainingEditorAgent


def gpt4_te_alpaca_lora_agent():
    manager_data = {
        "a suggestion for what to do next": "",
        "an inquisitive question": "My goal is to improve the model architecture of Alpaca-LoRA to make it a more powerful language model, without just making the model larger. Find the answer to that question in that context. If you can't, try another step in improving the language model.",
        "asking somebody to do something": "",
        "informative statements": "Ok, thanks. What's next?",
    }
    messages_path = "/selfmodifai/selfmodifai/prompts/messages.json"

    system_prompt = "You are part of an agent that is modifying the code of the model Alpaca-LoRA. The agent is in the Alpaca-LoRA directory. When you write code, that code will be executed and the output will be sent back to you."

    te_agent = Gpt4TrainingEditorAgent(manager_data, messages_path, system_prompt)
    te_agent.run()
