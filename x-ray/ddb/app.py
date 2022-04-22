import json
import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

# Path boto3 libraries to trace downstream calls (X-Ray)
patch_all()

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    # Instantiate a table resource object
    table = dynamodb.Table(event['TableName'])
    
    # Get table item
    response = table.get_item(
        Key={
            'Id': event['PartitionKey']
        })
    item = response['Item']

    return {
        'statusCode': 200,
        'body': item
    }
