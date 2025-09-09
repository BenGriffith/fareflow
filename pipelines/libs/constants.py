from decouple import config

DATA_ROOT = config("DATA_ROOT")
DATA_BUCKET = config("DATA_BUCKET")
MINIO_ENDPOINT = config("MINIO_ENDPOINT")
MINIO_ACCESS_KEY = config("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = config("MINIO_SECRET_KEY")
BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data"
RAW = f"{DATA_ROOT}/raw"
STAGING = f"{DATA_ROOT}/staging"
AUDIT = f"{DATA_ROOT}/audit"
CURATED = f"{DATA_ROOT}/curated"
