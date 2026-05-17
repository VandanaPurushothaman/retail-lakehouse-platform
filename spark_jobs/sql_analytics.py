from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("SQL Analytics Pipeline") \
    .getOrCreate()

# Read Silver Layer data
df = spark.read.parquet(
    "data/silver/retail_transactions"
)

print("\nSILVER DATA:")
df.show(5)

# Create Temporary SQL View
df.createOrReplaceTempView("retail_sales")

# -------------------------------
# Query 1 - Total Sales by Category
# -------------------------------

category_sales = spark.sql("""

SELECT
    category,
    SUM(total_amount) AS total_sales
FROM retail_sales
GROUP BY category
ORDER BY total_sales DESC

""")

print("\nTOTAL SALES BY CATEGORY:")
category_sales.show()

# -------------------------------
# Query 2 - Top Cities by Revenue
# -------------------------------

city_sales = spark.sql("""

SELECT
    city,
    SUM(total_amount) AS city_revenue
FROM retail_sales
GROUP BY city
ORDER BY city_revenue DESC

""")

print("\nTOP CITIES BY REVENUE:")
city_sales.show()

# -------------------------------
# Query 3 - Monthly Sales Trend
# -------------------------------

monthly_sales = spark.sql("""

SELECT
    transaction_month,
    SUM(total_amount) AS monthly_revenue
FROM retail_sales
GROUP BY transaction_month
ORDER BY transaction_month

""")

print("\nMONTHLY SALES TREND:")
monthly_sales.show()

# Stop Spark
spark.stop()