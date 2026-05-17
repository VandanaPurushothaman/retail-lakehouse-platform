import pandas as pd
import random
from datetime import datetime, timedelta
import uuid
import os


# Create output directory if not exists
os.makedirs("data/raw", exist_ok=True)

# Product catalog
products = [
    ("Laptop", "Electronics", 75000),
    ("Phone", "Electronics", 30000),
    ("Headphones", "Electronics", 5000),
    ("Monitor", "Electronics", 15000),
    ("Keyboard", "Electronics", 2000),
    ("Mouse", "Electronics", 1000),
    ("Shoes", "Fashion", 2500),
    ("T-Shirt", "Fashion", 800),
    ("Jeans", "Fashion", 1800),
    ("Watch", "Accessories", 5000)
]

# Cities
cities = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Hyderabad",
    "Pune"
]

# Payment methods
payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash"
]

# Generate records
data = []

for _ in range(1000):

    product = random.choice(products)

    quantity = random.randint(1, 5)

    transaction = {
        "transaction_id": str(uuid.uuid4()),
        "timestamp": (
            datetime.now() -
            timedelta(minutes=random.randint(0, 100000))
        ).strftime("%Y-%m-%d %H:%M:%S"),

        "product_name": product[0],
        "category": product[1],
        "price": product[2],
        "quantity": quantity,
        "total_amount": product[2] * quantity,

        "city": random.choice(cities),

        "payment_method": random.choice(payment_methods)
    }

    data.append(transaction)

# Convert to DataFrame
df = pd.DataFrame(data)

# Output file
output_path = "data/raw/retail_transactions.csv"

# Save CSV
df.to_csv(output_path, index=False)

print(f"Dataset created successfully at: {output_path}")
print(f"Total records: {len(df)}")