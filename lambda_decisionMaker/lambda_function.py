from __future__ import print_function
import json
from decimal import Decimal
import boto3

from utils import *



def generatePayload(val_time, val_sensor):
    payload = {
        'timestamp': val_time,
        'distance': val_sensor
    }
    fPayload = json.loads(json.dumps(payload), parse_float=Decimal)
    return fPayload

def pushToDynamoDB(val_time, val_sensor, endpoint = TABLE_ENDPOINT, table=TABLE_NAME):
    dynamodb = boto3.resource(
        service_name=SERVICE_NAME,
        region_name=REGION_NAME,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    table = dynamodb.Table(table)
    payload = generatePayload(val_time, val_sensor)
    response = table.put_item(Item=payload)
    return response

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    message = json.loads(event['Records'][0]['Sns']['Message'])
    timeVal = message["time"]
    sensorVal = message['value']
    if sensorVal<SENSOR_CUTOFF: 
        response = pushToDynamoDB(timeVal, sensorVal)
    return message