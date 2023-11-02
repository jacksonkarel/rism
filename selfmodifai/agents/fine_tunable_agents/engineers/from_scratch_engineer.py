from selfmodifai.agents.fine_tunable_agents.codellama_generate import codellama_generate


def from_scratch_engineer():
    with open("prompts/from_scratch/better_than_transformer.txt", "r") as f:
        prompt = f.read()
    codellama_generate(prompt)
