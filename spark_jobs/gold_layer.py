from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, avg

# Create Spark Session
spark = SparkSession.builder \
    .appName("Gold Layer Analytics") \
    .getOrCreate()

# Read Silver Layer
df = spark.read.parquet(
    "data/silver/retail_transactions"
)

print("\nSILVER DATA:\n")
df.show(5)

# ---------------------------------------------------
# 1. City-wise Revenue
# ---------------------------------------------------

city_revenue = df.groupBy("city") \
    .agg(
        sum("total_amount").alias("total_revenue")
    ) \
    .orderBy("total_revenue", ascending=False)

print("\nCITY-WISE REVENUE:\n")
city_revenue.show()

# ---------------------------------------------------
# 2. Product Performance
# ---------------------------------------------------

product_performance = df.groupBy("product") \
    .agg(
        sum("quantity").alias("total_quantity_sold"),
        sum("total_amount").alias("total_sales")
    ) \
    .orderBy("total_sales", ascending=False)

print("\nPRODUCT PERFORMANCE:\n")
product_performance.show()

# ---------------------------------------------------
# 3. Payment Method Analysis
# ---------------------------------------------------

payment_analysis = df.groupBy("payment_method") \
    .agg(
        count("*").alias("transaction_count"),
        avg("total_amount").alias("avg_transaction_value")
    )

print("\nPAYMENT METHOD ANALYSIS:\n")
payment_analysis.show()

# ---------------------------------------------------
# Write Gold Layer
# ---------------------------------------------------

city_revenue.write \
    .mode("overwrite") \
    .parquet("data/gold/city_revenue")

product_performance.write \
    .mode("overwrite") \
    .parquet("data/gold/product_performance")

payment_analysis.write \
    .mode("overwrite") \
    .parquet("data/gold/payment_analysis")

print("\nGold Layer analytics stored successfully.")

spark.stop()