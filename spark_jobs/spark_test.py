# Import SparkSession
# SparkSession is the main entry point for working with Spark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col


# Create Spark Session
# This initializes the Spark application

spark = (
    SparkSession.builder
    .appName("Retail Lakehouse Test")
    .master("local[*]")
    .getOrCreate()
)


# Create Sample Data
# This simulates small retail transaction data

sample_data = [
    (1, "Laptop", 75000),
    (2, "Phone", 30000),
    (3, "Headphones", 5000),
    (4, "Monitor", 15000)
]


# Define column names

columns = ["product_id", "product_name", "price"]


# Create Spark DataFrame

df = spark.createDataFrame(sample_data, columns)


# Display DataFrame

print("\nDisplaying Retail Data:\n")

df.show()


# Print Schema
# Schema means structure of the data

print("\nSchema of Data:\n")

df.printSchema()



# Transformation Example
# Transformations are lazy operations

filtered_df = df.filter(df.price > 10000)

print("\nTransformation Created Successfully")


# Action Trigger
# show() is an action that triggers execution

print("\nFiltered Products:\n")

filtered_df.show()

# Stop Spark Session
# Best practice to release resources

spark.stop()