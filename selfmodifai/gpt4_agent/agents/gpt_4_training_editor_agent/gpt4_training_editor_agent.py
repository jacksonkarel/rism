from selfmodifai.gpt4_agent.gpt4_agent import Gpt4Agent


class Gpt4TrainingEditorAgent:
    def __init__(self, manager_data, messages_path, system_prompt):
        self.manager_data = manager_data
        self.messages_path = messages_path
        self.system_prompt = system_prompt

    def run(self):
        gpt4_agent = Gpt4Agent(self.manager_data, self.messages_path, self.system_prompt)
        gpt4_agent.run()
