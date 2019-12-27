#!/bin/bash



aws cloudformation create-change-set --stack-name my-application --change-set-type CREATE --change-set-name my-change-set --template-body file://s3.yaml --capabilities CAPABILITY_IAM --parameters ParameterKey=BucketName,ParameterValue=my-bucket-12 ParameterKey=TableName,ParameterValue=my-db-12 ParameterKey=ListenerLambdaName,ParameterValue=lambda.zip                                                                       
aws cloudformation execute-change-set --change-set-name my-change-set --stack-name my-application
