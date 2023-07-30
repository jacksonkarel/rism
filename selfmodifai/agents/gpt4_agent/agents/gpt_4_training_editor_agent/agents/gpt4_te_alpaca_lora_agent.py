from selfmodifai.agents.gpt4_agent.agents.gpt_4_training_editor_agent.agents.github_model_agent import GithubModelAgent
from selfmodifai.agents.gpt4_agent.agents.gpt_4_training_editor_agent.gpt4_training_editor_agent import (
    Gpt4TrainingEditorAgent,
)


def gpt4_te_alapca_lora_agent():
    gh_repo = "git@github.com:jacksonkarel/selfmodifai-alpaca-lora.git"

    manager_data = {
        "a suggestion for what to do next": "",
        "an inquisitive question": "My goal is to improve the model architecture of Alpaca-LoRA to make it a more powerful language model, without just making the model larger. Find the answer to that question in that context. If you can't, try another step in improving the language model.",
        "asking somebody to do something": "",
        "informative statements": "Ok, thanks. What's next?",
    }
    messages_path = "/selfmodifai/selfmodifai/prompts/alpaca_lora/training_editor.json"

    system_prompt = "You are part of an agent that is modifying the code of the model Alpaca-LoRA. The agent is in the Alpaca-LoRA directory. When you write code, that code will be executed and the output will be sent back to you."

    agent = GithubModelAgent(gh_repo, manager_data, messages_path, system_prompt, Gpt4TrainingEditorAgent)
    agent.run()
