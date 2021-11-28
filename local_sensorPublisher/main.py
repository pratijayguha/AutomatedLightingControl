from utils import *

# Connecting to AWS to use SNS
sns = boto3.resource(
    service_name=SERVICE_NAME,
    region_name=REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

while True:
    # Get distance reading
    result = getDistanceReading(ECHO_PIN, TRIGGER_PIN)
    # Time stored as a numerical value
    t_now = time.time()
    # Stitching the data we wamt to share in the form of a json dump
    data = {"time" : t_now,
            "value" : result}        
    payload = json.dumps(data)
    # Publishing to AWS
    pubStatus = publishToTopic(sns, payload, TOPIC_ARN)
    # Printing Confirmation - Indicates error if pubStatus is False
    print(result, pubStatus)
