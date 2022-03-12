#!/bin/bash
set -xeuo pipefail
export IMAGE=combinatorml/jupyterlab-tensorflow-opencv:0.8
docker build -t $IMAGE .
docker push $IMAGE
