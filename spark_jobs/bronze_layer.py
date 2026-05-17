from pyspark.sql import SparkSession
from configs.logger_config import logger


# Start Logging
logger.info("Bronze Layer Pipeline Started")


# Create Spark Session
spark = SparkSession.builder \
    .appName("Bronze Layer Pipeline") \
    .getOrCreate()


# Read raw CSV data
df = spark.read.csv(
    "data/raw/retail_transactions.csv",
    header=True,
    inferSchema=True
)


print("\nRAW DATA:")
df.show(5)

logger.info("Raw data loaded successfully")


print("\nSCHEMA:")
df.printSchema()

logger.info("Schema printed successfully")


# Write to Bronze Layer in Parquet format
df.write.mode("overwrite").parquet(
    "data/bronze/retail_transactions"
)

print("\nBronze Layer Created Successfully")

logger.info("Bronze Layer parquet files created successfully")


# Stop Spark session
spark.stop()

logger.info("Spark Session Stopped")
logger.info("Bronze Layer Pipeline Completed Successfully")