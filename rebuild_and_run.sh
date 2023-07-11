#!/bin/bash

# The name of your Docker image
IMAGE_NAME="selfmodifai"

# The name of your Docker container
CONTAINER_NAME="selfmodifai"

# Stop the running container
docker stop $CONTAINER_NAME

# Remove the container
docker rm $CONTAINER_NAME

docker system prune

# Remove the image
docker rmi $IMAGE_NAME

# Build the image
docker build -t $IMAGE_NAME .

# Run the container
docker run -e OPENAI_API_KEY -d -it --name $CONTAINER_NAME $IMAGE_NAME

docker exec -it $CONTAINER_NAME bash