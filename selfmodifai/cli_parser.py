import argparse
from selfmodifai.agents.hf_agent.llama2_agent.llama2_agent import llama2_agent
from selfmodifai.agents.hf_agent.llama2_agent.generation.sagemaker.llama2_sagemaker_deploy import (
    llama2_sagemaker_deploy,
)


def cli_parser():
    sm_parser = argparse.ArgumentParser(description="Autonomous AI agents modifying the training code of ML models")

    sm_parser.add_argument("task", action="store", choices=["deploy_model", "run"], help="Agent type")

    args = sm_parser.parse_args()

    task = args.task

    if task == "deploy_model":
        llama2_sagemaker_deploy()

    elif task == "run":
        llama2_agent()
