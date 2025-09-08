import boto3

from pipelines.libs import constants


def s3_client():
    s3 = boto3.client(
        "s3",
        endpoint_url=constants.MINIO_ENDPOINT,
        aws_access_key_id=constants.MINIO_ACCESS_KEY,
        aws_secret_access_key=constants.MINIO_SECRET_KEY,
    )
    return s3
