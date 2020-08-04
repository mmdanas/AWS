#!/usr/bin/python3.6
#aws lambda code for sending message to slack channle
#sns subscription must be configured to link the lambda function to sns
#webhook url for slack must be configured inorder to send the notification
import urllib3
import json
http = urllib3.PoolManager()
def lambda_handler(event, context):
    url = "#webhookurl for slack channel"
    msg = {
        "channel": "#channel name",
        "username": "#Channel username",
        "text": event['Records'][0]['Sns']['Message'],
        "icon_emoji": ":alien:"
        #any slack emoji can be given as icon.
    }

    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST',url, body=encoded_msg)
    print({
        "message": event['Records'][0]['Sns']['Message'],
        "status_code": resp.status,
        "response": resp.data
    })
