import boto3
from botocore.exceptions import ClientError, EndpointConnectionError

from pipelines.libs import constants


def main():
    s3 = boto3.client(
        "s3",
        endpoint_url=constants.MINIO_ENDPOINT,
        aws_access_key_id=constants.MINIO_ACCESS_KEY,
        aws_secret_access_key=constants.MINIO_SECRET_KEY,
    )

    try:
        names = [bucket["Name"] for bucket in s3.list_buckets().get("Buckets", [])]
        if constants.DATA_BUCKET in names:
            print(f"Bucket already exists: {constants.DATA_BUCKET}")
            return 0

        s3.create_bucket(Bucket=constants.DATA_BUCKET)
        print(f"Created bucket: {constants.DATA_BUCKET}")

    except EndpointConnectionError as error:
        print(f"Could not reach MinIO at {constants.MINIO_ENDPOINT}: {error}")
        return 2
    except ClientError as error:
        print(f"S3 error: {error}")
        return 3


if __name__ == "__main__":
    main()
