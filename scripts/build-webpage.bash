#!/bin/bash

cd ../cf

echo "uploading CF config"
aws cloudformation create-change-set --stack-name my-temp-render --change-set-type CREATE --change-set-name my-render-change-set --template-body file://rendertemp.yaml --capabilities CAPABILITY_IAM 

sleep 5

echo "executing CF config"

aws cloudformation execute-change-set --change-set-name my-render-change-set --stack-name my-temp-render

echo "Waiting for response"

aws cloudformation wait stack-create-complete --stack-name my-temp-render

echo "creation complete"

bucketname=`aws cloudformation list-exports --query "Exports[?Name=='TempRenderBucket'].Value" --output text```
echo bucketname

aws s3 cp ../render-www s3://${bucketname} --exclude "venv/*" --exclude ".idea/*" --recursive

echo "files uploaded"


