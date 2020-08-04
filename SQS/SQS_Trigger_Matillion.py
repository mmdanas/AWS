import boto3
#import json to pass our messages in json format
import json
sqs = boto3.resource('sqs')
#mention the queue name where the message needs to be sent
queue = sqs.get_queue_by_name(QueueName='#queuename')
#pass your message here which should be your job details
#this can also be variablized. Pass job variables if it has been created
j_msg = {
 "created":"-",
 "group":groupName,
 "project":"#projectname",
 "version":"#version",
 "environment":"#enviromentname",
 "job":"#jobtotrigger"
}
#multiple messages can be sent which can be treated as multiple triggers
k_msg = {
 "created":"-",
 "group":groupName,
 "project":"#projectname",
 "version":"#version",
 "environment":"#enviromentname",
 "job":"#jobtotrigger"
}
#A response is generated only if a message is sent
response1 = queue.send_message(MessageBody=json.dumps(j_msg))
response2 = queue.send_message(MessageBody=json.dumps(k_msg))
print(response1['MessageId'])
print(response2['MessageId'])
