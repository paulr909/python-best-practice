import pytest

from bucket.models import SampleSQSClient


@pytest.fixture
def queue_name():
    return "test-queue"


@pytest.fixture
def sqs_test(sqs_client, queue_name):
    sqs_client.create_queue(QueueName=queue_name)
    yield


def test_get_queue_url(sqs_client, sqs_test):
    sqs_client = SampleSQSClient()
    queue_url = sqs_client.get_queue_url(queue_name="test-queue")
    assert "test-queue" in queue_url


def test_receive_message(sqs_client, sqs_test):
    client = SampleSQSClient()
    queue_url = client.get_queue_url(queue_name="pro-test")

    sqs_client.send_message(QueueUrl=queue_url, MessageBody="high importance")

    response = client.receive_message(queue_url=queue_url)
    assert response["Messages"][0]["Body"] == "high importance"
