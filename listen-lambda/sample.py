import boto3
import json
import decimal

from convertdict import convert

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


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
        print("dict", dict)

        dataObj = convert(dict)

        table = dynamodb.Table('my-db-12')
        response = table.put_item(
            Item=dataObj
        )
        print('Successful put')
        print(json.dumps(response, indent=4, cls=DecimalEncoder))


