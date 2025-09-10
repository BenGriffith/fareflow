from pyspark.sql import SparkSession

from pipelines.libs import constants


def build_spark(app_name):
    spark = (
        SparkSession.builder.appName(app_name)
        .config("spark.hadoop.fs.s3a.endpoint", constants.MINIO_HOSTPORT)
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")
        .config(
            "spark.hadoop.fs.s3a.aws.credentials.provider",
            "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider",
        )
        .config("spark.hadoop.fs.s3a.access.key", constants.MINIO_ACCESS_KEY)
        .config("spark.hadoop.fs.s3a.secret.key", constants.MINIO_SECRET_KEY)
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
        .getOrCreate()
    )
    return spark
