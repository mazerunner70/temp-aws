#1/bin/bash

cd ../listen-lambda

zip ../scripts/lambda.zip *

cd ../scripts
aws s3 mv lambda.zip s3://wils-lambda-zips

