import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import input_file_name, split, col


args = getResolvedOptions(sys.argv, ['JOB_NAME'])   #starting_of_glue_job
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


source_bucket = "s3://spaluri-de-on-youtube-raw-useast1-dev/youtube/raw_statistics/"
target_bucket = "s3://spaluri-de-on-youtube-cleansed-useast1-dev/youtube/raw_statistics/"


df = spark.read.option("header", "true").option("recursiveFileLookup", "true").csv(source_bucket)

df = df.withColumn("region", split(input_file_name(), '/').getItem(-2))
df = df.withColumn("category_id", col("category_id").cast("int"))

df.write.mode("overwrite").parquet(target_bucket)

job.commit()