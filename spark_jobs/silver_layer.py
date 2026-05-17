from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, year, month

# Create Spark Session
spark = SparkSession.builder \
    .appName("Silver Layer Pipeline") \
    .getOrCreate()

# Read Bronze Layer
df = spark.read.parquet(
    "data/bronze/retail_transactions"
)

print("\nBRONZE DATA:\n")
df.show(5)

# Remove duplicates
df = df.dropDuplicates(["transaction_id"])

# Remove null values
df = df.dropna()

# Convert timestamp column
df = df.withColumn(
    "timestamp",
    to_timestamp(col("timestamp"))
)

# Create derived columns
df = df.withColumn("year", year(col("timestamp")))
df = df.withColumn("month", month(col("timestamp")))

print("\nCLEANED SILVER DATA:\n")
df.show(5)

# Write Silver Layer
output_path = "data/silver/retail_transactions"

df.write \
    .mode("overwrite") \
    .parquet(output_path)

print(f"\nSilver Layer stored at: {output_path}")

spark.stop()