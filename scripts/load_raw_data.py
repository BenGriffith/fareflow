import argparse

import requests
from botocore.exceptions import ClientError

from pipelines.libs import constants
from scripts.helpers import s3_client


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--service", required=True, choices=["yellow", "green", "fhv"])
    ap.add_argument("--month", required=True, help="YYYY-MM")
    args = ap.parse_args()

    filename = f"{args.service}_tripdata_{args.month}.parquet"
    url = f"{constants.BASE_URL}/{filename}"
    key = f"raw/taxi/{args.service}/{args.month}/{filename}"
    s3 = s3_client()

    try:
        s3.head_object(Bucket=constants.DATA_BUCKET, Key=key)
        print(f"File exists: s3://{constants.DATA_BUCKET}/{key}")
    except ClientError as error:
        if error.response["Error"]["Code"] != "404":
            raise

    with requests.get(url, stream=True) as r:
        r.raise_for_status()

        s3.upload_fileobj(
            Fileobj=r.raw,
            Bucket=constants.DATA_BUCKET,
            Key=key,
        )

        print(f"File uploaded: s3://{constants.DATA_BUCKET}/{key}")


if __name__ == "__main__":
    main()
