import json
import os
import boto3
from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri


def llama2_sagemaker_deploy():
    iam_client = boto3.client("iam")
    role = iam_client.get_role(RoleName="AmazonSageMaker-ExecutionRole-20210712T131052")["Role"]["Arn"]

    # Hub Model configuration. https://huggingface.co/models
    hub = {
        "HF_MODEL_ID": "meta-llama/Llama-2-7b-chat-hf",
        "SM_NUM_GPUS": json.dumps(1),
        "HUGGING_FACE_HUB_TOKEN": os.environ.get("HF_TOKEN"),
    }

    # create Hugging Face Model Class
    huggingface_model = HuggingFaceModel(
        image_uri=get_huggingface_llm_image_uri("huggingface", version="0.9.3"),
        env=hub,
        role=role,
    )

    # deploy model to SageMaker Inference
    huggingface_model.deploy(
        initial_instance_count=1,
        instance_type="ml.g5.2xlarge",
        container_startup_health_check_timeout=300,
    )
