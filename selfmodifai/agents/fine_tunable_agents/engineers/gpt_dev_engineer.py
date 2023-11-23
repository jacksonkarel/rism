from selfmodifai.agents.fine_tunable_agents.codellama_generate import codellama_generate


def gpt_dev_engineer():
    with open("prompts/nanogpt/engineer.txt", "r") as f:
        prompt = f.read()
    codellama_generate(prompt)
