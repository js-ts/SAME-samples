#!/bin/bash
set -xeuo pipefail
export IMAGE=combinatorml/jupyterlab-tensorflow-opencv:0.6
docker build -t $IMAGE .
docker push $IMAGE
