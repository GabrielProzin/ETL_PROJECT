from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.extract.extract import extract_data
from src.transform.transform import transform_data
from src.load.load import load_data

with DAG(
    dag_id="pipeline_vendas",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="extract",
        python_callable=extract_data
    )

    t2 = PythonOperator(
        task_id="transform",
        python_callable=transform_data
    )

    t3 = PythonOperator(
        task_id="load",
        python_callable=load_data
    )

    t1 >> t2 >> t3