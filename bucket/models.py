import boto3


class S3BucketModel(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def save(self):
        s3 = boto3.client("s3", region_name="us-east-1")
        s3.put_object(Bucket="pro-bucket", Key=self.name, Body=self.value)


class SampleSQSClient:
    def __init__(self, region_name="us-east-1"):
        self.client = boto3.client("sqs", region_name=region_name)

    def get_queue_url(self, queue_name):
        response = self.client.create_queue(QueueName=queue_name)
        return response["QueueUrl"]

    def receive_message(self, queue_url):
        return self.client.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
        )
