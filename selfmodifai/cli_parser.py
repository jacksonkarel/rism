import argparse
from selfmodifai.gpt4_agent import gpt4_agent

def cli_parser():
    selfm_parser = argparse.ArgumentParser(description="LLM-powered AI agents modifying the source code of other LLMs")

    selfm_parser.add_argument('messages_path', help='Messages json path')

    args = selfm_parser.parse_args()

    messages_path = args.messages_path
    gpt4_agent(messages_path)