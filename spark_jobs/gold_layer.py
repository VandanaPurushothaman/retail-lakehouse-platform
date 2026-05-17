from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, count
from configs.logger_config import logger


# Create Spark Session
spark = SparkSession.builder \
    .appName("Gold Layer Pipeline") \
    .getOrCreate()

logger.info("Gold Layer Pipeline Started")


# Read Silver Data
df = spark.read.parquet(
    "data/silver/retail_transactions"
)

logger.info("Silver data loaded successfully")


print("\nSILVER DATA:")
df.show(5)


# Create city-wise sales summary
city_sales_df = df.groupBy("city").agg(
    sum("total_amount").alias("total_revenue"),
    avg("total_amount").alias("average_sales"),
    count("transaction_id").alias("total_transactions")
)

logger.info("City sales aggregation completed")


print("\nCITY SALES SUMMARY:")
city_sales_df.show()


# Write Gold Layer
city_sales_df.write.mode("overwrite").parquet(
    "data/gold/city_sales_summary"
)

logger.info("Gold Layer created successfully")


print("\nGold Layer Created Successfully")


# Stop Spark Session
spark.stop()

logger.info("Spark Session Stopped")