import boto3

# Replace these with your own AWS credentials
aws_access_key = 'AKIAZWM3B4WZ4OC6K55C'
aws_secret_key = 'oOMZlp0u4codgQTLqAWmsTD0VyVOFZJ1x7ufB3iN'
aws_region = 'ap-south-1'   # Replace with your desired AWS region

# Create an SQS client
sqs = boto3.client('sqs', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

# Replace 'your-queue-url' with the URL of your existing SQS queue
fifo_queue_url = 'https://sqs.ap-south-1.amazonaws.com/666581984691/Batch-Schedule.fifo'

# Receive messages from the queue
def receive_messages():
    response = sqs.receive_message(
        QueueUrl=fifo_queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=5  # Wait up to 5 seconds for a message
    )

    if 'Messages' in response:
        for message in response['Messages']:
            print("Received Message:", message['Body'])
            # Delete the received message from the queue
            sqs.delete_message(
                QueueUrl=fifo_queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )
    else:
        print("No messages in queue.")

def main():
    receive_messages()

if __name__ == "__main__":
    main()
