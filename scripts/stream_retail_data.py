import json
import random
import time
from datetime import datetime
import uuid
import os

# Create raw data folder if not exists
RAW_DATA_PATH = "data/raw"
os.makedirs(RAW_DATA_PATH, exist_ok=True)

output_file = os.path.join(RAW_DATA_PATH, "streaming_retail_data.json")

cities = ["Bangalore", "Mumbai", "Delhi", "Chennai", "Hyderabad", "Pune"]

products = [
    ("Laptop", "Electronics"),
    ("Mobile", "Electronics"),
    ("Shoes", "Fashion"),
    ("T-Shirt", "Fashion"),
    ("Watch", "Accessories"),
    ("Headphones", "Electronics")
]

payment_methods = ["UPI", "Credit Card", "Debit Card", "Cash"]

print("Streaming retail data started...\n")

while True:

    product_name, category = random.choice(products)

    event = {
        "transaction_id": str(uuid.uuid4()),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "city": random.choice(cities),
        "product": product_name,
        "category": category,
        "quantity": random.randint(1, 5),
        "price": random.randint(500, 50000),
        "payment_method": random.choice(payment_methods)
    }

    event["total_amount"] = event["quantity"] * event["price"]

    with open(output_file, "a") as f:
        f.write(json.dumps(event) + "\n")

    print(f"Generated Event: {event}")

    time.sleep(2)