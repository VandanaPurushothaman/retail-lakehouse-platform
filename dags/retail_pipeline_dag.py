from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "vandana",
    "start_date": datetime(2025, 1, 1)
}

with DAG(
    dag_id="retail_lakehouse_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    bronze_task = BashOperator(
        task_id="bronze_layer",
        bash_command="python /app/spark_jobs/bronze_layer.py"
    )

    silver_task = BashOperator(
        task_id="silver_layer",
        bash_command="python /app/spark_jobs/silver_layer.py"
    )

    gold_task = BashOperator(
        task_id="gold_layer",
        bash_command="python /app/spark_jobs/gold_layer.py"
    )

    analytics_task = BashOperator(
        task_id="sql_analytics",
        bash_command="python /app/spark_jobs/sql_analytics.py"
    )

    bronze_task >> silver_task >> gold_task >> analytics_task