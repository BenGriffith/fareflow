from botocore.exceptions import ClientError, EndpointConnectionError

from pipelines.libs import constants
from scripts.helpers import s3_client


def main():
    try:
        s3 = s3_client()
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
    raise SystemExit(main())
