#!/bin/bash
set -xeuo pipefail
export IMAGE=combinatorml/jupyterlab-tensorflow-opencv:0.4
docker build -t $IMAGE .
docker push $IMAGE
