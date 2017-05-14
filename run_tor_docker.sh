#!/bin/bash
CONTAINER_NAME=${1:-"myproxy"}
docker run -it -p 8118:8118 -p 9050:9050 -d --name "$CONTAINER_NAME" dperson/torproxy

if [ $? == 0 ];
then
        echo "Container running ! container's name: $CONTAINER_NAME"
else
        echo "Something went wrong."
fi
