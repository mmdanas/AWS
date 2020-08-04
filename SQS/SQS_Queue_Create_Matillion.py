import boto.sqs
#conn = boto.sqs.connect_to_region("Region")
conn = boto.sqs.connect_to_region("#region")
#queue = conn.create_queue("Queue-Name")
queue = conn.create_queue("#queuename")
