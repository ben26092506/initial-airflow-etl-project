from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='hello_dag',
    start_date=datetime(2023, 1, 1),
    schedule='@once',
    catchup=False
) as dag:

    hello = BashOperator(
        task_id='say_hello',
        bash_command='echo "Hello, Airflow!"'
    )