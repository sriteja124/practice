#!/bin/bash

echo helloworld
kubectl apply -f her.yaml
echo success
echo $PWD
mkdir 0
cd ./0
echo $PWD
