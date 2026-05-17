# Retail Lakehouse Platform

End-to-end Data Engineering project built using PySpark, Docker, and Airflow implementing Medallion Architecture (Bronze, Silver, Gold layers).

---

## Tech Stack

- Python
- PySpark
- Docker
- Apache Airflow
- Parquet
- Pandas
- Logging

---

## Architecture

Raw CSV Data
        ↓
Bronze Layer (Raw Parquet)
        ↓
Silver Layer (Cleaned Data)
        ↓
Gold Layer (Business Aggregations)
        ↓
Analytics & Reporting

---

## Features

- Dockerized Spark environment
- Medallion Architecture implementation
- Data cleaning and transformation
- Aggregated business analytics
- Logging support
- Airflow DAG orchestration
- Parquet-based storage

---

## Project Structure

```text
retail-lakehouse-platform/
│
├── dags/
├── spark_jobs/
├── data/
├── logs/
├── configs/
├── docker/
├── sql/
└── notebooks/