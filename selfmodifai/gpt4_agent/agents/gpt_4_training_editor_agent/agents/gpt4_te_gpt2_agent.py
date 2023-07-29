from selfmodifai.gpt4_agent.agents.gpt_4_training_editor_agent.agents.github_model_agent import GithubModelAgent
from selfmodifai.gpt4_agent.agents.gpt_4_training_editor_agent.gpt4_training_editor_agent import Gpt4TrainingEditorAgent


def gpt4_te_gpt2_agent():
    gh_repo = "git@github.com:jacksonkarel/selfmodifai-gpt-2.git"
    dir_path = "/selfmodifai/selfmodifai-gpt-2"

    manager_data = {
        "a suggestion for what to do next": "",
        "an inquisitive question": "My goal is to improve the model architecture of GPT-2 to make it a more powerful language model, without just making the model larger. Find the answer to that question in that context. If you can't, try another step in improving the language model.",
        "asking somebody to do something": "",
        "informative statements": "Ok, thanks. What's next?",
    }
    messages_path = "/selfmodifai/selfmodifai/prompts/gpt2/training_editor.json"

    system_prompt = "You are part of an agent that is modifying the code of the model GPT-2. The agent is in the GPT-2 directory. When you write code, that code will be executed and the output will be sent back to you."

    agent = GithubModelAgent(gh_repo, dir_path, manager_data, messages_path, system_prompt, Gpt4TrainingEditorAgent)
    agent.run()
