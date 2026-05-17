from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp
from configs.logger_config import logger


# Create Spark Session
spark = SparkSession.builder \
    .appName("Silver Layer Pipeline") \
    .getOrCreate()


logger.info("Silver Layer Pipeline Started")


# Read Bronze Data
df = spark.read.parquet(
    "data/bronze/retail_transactions"
)

logger.info("Bronze data loaded successfully")


print("\nBRONZE DATA:")
df.show(5)


# Remove null values
clean_df = df.dropna()

logger.info("Null values removed")


# Remove duplicate transactions
clean_df = clean_df.dropDuplicates(["transaction_id"])

logger.info("Duplicate records removed")


# Add processing timestamp
clean_df = clean_df.withColumn(
    "processed_timestamp",
    current_timestamp()
)

logger.info("Processed timestamp column added")


print("\nCLEANED DATA:")
clean_df.show(5)


print("\nSILVER SCHEMA:")
clean_df.printSchema()


# Write Silver Layer
clean_df.write.mode("overwrite").parquet(
    "data/silver/retail_transactions"
)

logger.info("Silver Layer created successfully")


print("\nSilver Layer Created Successfully")


# Stop Spark Session
spark.stop()

logger.info("Spark Session Stopped")