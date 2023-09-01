import os
from git import Repo


class GithubModelAgent:
    def __init__(self, gh_repo, manager_data, messages_path, system_prompt, training_editor_agent) -> None:
        self.gh_repo = gh_repo
        self.manager_data = manager_data
        self.messages_path = messages_path
        self.system_prompt = system_prompt
        self.training_editor_agent = training_editor_agent

    def run(self):
        Repo.clone_from(self.gh_repo, "/selfmodifai/model")

        te_agent = self.training_editor_agent(self.manager_data, self.messages_path, self.system_prompt)
        te_agent.run()
