import boto3
from moto import mock_s3

from bucket.models import S3BucketModel


@mock_s3
def test_model_save():
    conn = boto3.resource("s3", region_name="us-east-1")
    # We need to create the bucket since this is all in Moto's 'virtual' AWS account
    conn.create_bucket(Bucket="pro-bucket")
    model_instance = S3BucketModel("Profusion", "is awesome")
    model_instance.save()
    body = conn.Object("pro-bucket", "Profusion").get()["Body"].read().decode("utf-8")
    assert body == "is awesome"


def test_create_bucket(s3):
    # s3 is a fixture defined above that yields a boto3 s3 client.
    # Feel free to instantiate another boto3 S3 client -- Keep note of the region though.
    s3.create_bucket(Bucket="test-bucket")

    result = s3.list_buckets()
    assert len(result["Buckets"]) == 1
    assert result["Buckets"][0]["Name"] == "test-bucket"
