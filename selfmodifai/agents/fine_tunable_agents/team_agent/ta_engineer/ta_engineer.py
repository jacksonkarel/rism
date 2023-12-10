from selfmodifai.agents.fine_tunable_agents.team_agent.ta_engineer.complete_the_code import complete_the_code


def ta_engineer(brainstorm_response_content, messages, pattern):
    new_messages = [
        {"role": "assistant", "content": brainstorm_response_content},
        {"role": "user", "content": "Write the code for this in PyTorch"},
    ]
    messages += new_messages
    complete_code = complete_the_code(messages, pattern)
