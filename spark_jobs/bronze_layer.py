from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("Bronze Layer Streaming Pipeline") \
    .getOrCreate()

# Read streaming JSON data
df = spark.read.json(
    "data/raw/streaming_retail_data.json"
)

print("\nRAW STREAMING DATA:\n")

df.show(5)

# Write Bronze Layer
output_path = "data/bronze/retail_transactions"

df.write \
    .mode("overwrite") \
    .parquet(output_path)

print(f"\nBronze Layer stored at: {output_path}")

spark.stop()