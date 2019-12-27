import boto3
import re
import requests
from requests_aws4auth import AWS4Auth
import json

region = 'eu-west-1'  # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = 'https://search-es-temp-6k7vrsrw544xrx5e3gnju3yvby.eu-west-1.es.amazonaws.com'  # the Amazon ES domain, including https://
index = 'sensor_index'
type = '_doc'
url = host + '/' + index + '/' + type

headers = {"Content-Type": "application/json"}

s3 = boto3.client('s3')

# Regular expressions used to parse some simple log lines
ip_pattern = re.compile('(\d+\.\d+\.\d+\.\d+)')
time_pattern = re.compile('\[(\d+\/\w\w\w\/\d\d\d\d:\d\d:\d\d:\d\d\s-\d\d\d\d)\]')
message_pattern = re.compile('\"(.+)\"')


# Lambda execution starts here
def handler(event, context):
    for record in event['Records']:

        # Get the bucket name and key for the new file
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # Get, read, and split the file into lines
        obj = s3.get_object(Bucket=bucket, Key=key)
        body = obj['Body'].read()
        dict = json.loads(body)
        print "dict", dict
        r = requests.post(url, auth=awsauth, json=dict, headers=headers)
        print "response", r
        print "text", r.text