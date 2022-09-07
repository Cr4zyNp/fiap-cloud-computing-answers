import json
from sqsHandler import SqsHandler
import os

def enviarSQSHandler(event,context):

    print(json.dumps(event))
    awsRegion = os.environ.get('awsRegion', '')
    awsAccountId = os.environ.get('awsAccountId', '')
    
    sqs = SqsHandler("https://sqs."+awsRegion+".amazonaws.com/"+awsAccountId+"/espera-entrega")

    #sqs = SqsHandler("https://sqs.us-east-1.amazonaws.com/648865203648/espera-entrega")
    
    sqs.send(str(event['detail']))
        
    return event