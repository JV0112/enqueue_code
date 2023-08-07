import boto3

# Replace these with your own AWS credentials
aws_access_key = 'AKIAZWM3B4WZ4OC6K55C'
aws_secret_key = 'oOMZlp0u4codgQTLqAWmsTD0VyVOFZJ1x7ufB3iN'
aws_region = 'ap-south-1'  # Replace with your desired AWS region

# Create an SQS client
sqs = boto3.client('sqs', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

# Replace 'your-queue-url' with the URL of your existing SQS queue
fifo_queue_url = 'https://sqs.ap-south-1.amazonaws.com/666581984691/Batch-Schedule.fifo'
message_body = 'Hello, I am here. Where are you!'
message_group_id = 'group-1' 


# response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
response = sqs.send_message(
    QueueUrl=fifo_queue_url,
    MessageBody=message_body,
    MessageGroupId=message_group_id
)


