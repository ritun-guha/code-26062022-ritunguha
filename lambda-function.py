import json
import boto3

BUCKET_NAME = 'Ref_LambdaFunctionS3Bucket'

def s3_client():
    s3 = boto3.client('s3')
    return s3

def put_object_to_bucket(Body):
  object_key = 's3.md'
  return s3_client().put_object( Body=Body, Bucket=BUCKET_NAME, Key=object_key)

def lambda_handler(event, context):
    for record in event['Records']:
        payload = record["body"]
        put_object_to_bucket(payload)
        print(str(payload))
