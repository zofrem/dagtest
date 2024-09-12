from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from my_python_logic import my_task


with DAG(
    dag_id='my_simple_dag',
    start_date=datetime(2023, 9, 1),
    schedule_interval='@daily',
    catchup=False,
) as dag:
    
    task = PythonOperator(
        task_id='run_my_task',
        python_callable=my_task
    )