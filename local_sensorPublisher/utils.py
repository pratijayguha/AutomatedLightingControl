import json
from gpiozero import DistanceSensor
import time
import boto3


# Standard Variables - does not change from account to account
SERVICE_NAME='sns'
ECHO_PIN = 17
TRIGGER_PIN = 4


# Custom variables - changes from account to account
REGION_NAME='us-XXX-X'
AWS_ACCESS_KEY_ID='XXXXXXXXXXXXXXXXXXXX'
AWS_SECRET_ACCESS_KEY='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
TABLE_ENDPOINT = 'XXXXXXXXXXXXXXXXXX.iot.us-XXXX-X.amazonaws.com'
TABLE_NAME = 'iiot_termProject'
TOPIC_ARN = 'arn:aws:sns:us-XXXX-X:XXXXXXXXXXXX:iiot_termProject'


# Function to get a reading from ultrasonic sensor
def getDistanceReading(echoPin, triggerPin):
    sensor = DistanceSensor(echo=echoPin, trigger=triggerPin)
    return sensor.distance


# Function to publish a payload to a topic
def publishToTopic(sns, payload, topic_arn):

    topic = sns.Topic(topic_arn)
    message = payload
    response = topic.publish(Message=message)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return True
    else:
        return False