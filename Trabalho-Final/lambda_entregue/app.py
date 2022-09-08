import json
from sqsHandler import SqsHandler
import os


def entregueHandler(event,context):
    awsRegion = os.environ.get('awsRegion', '')
    awsAccountId = os.environ.get('awsAccountId', '')
    
    sqs = SqsHandler("https://sqs."+awsRegion+".amazonaws.com/"+awsAccountId+"/espera-entrega")

    while(True):
        response = sqs.getMessage(1)
        print(response)
        mensagem = response.get('Messages')
        if mensagem:
            mensagens = []
            for msg in response['Messages']:
                #mensagens.append({'Id':msg['MessageId'], 'ReceiptHandle':msg['ReceiptHandle']})    
                #sqs.deleteMessage(mensagens)
                sqs.deleteMessage(msg['ReceiptHandle'])
        else:
            break