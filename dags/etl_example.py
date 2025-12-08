from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os

DATA_DIR = '/home/ben/airflow/data'

def extract():
    df = pd.DataFrame({
        'name': ['Ina', 'Fiona', 'Alice'],
        'age': [17, 23, 25]
    })
    df.to_csv(f'{DATA_DIR}/raw.csv', index=False)
    print('Extract complete - raw.csv created.')

def transform():
    df = pd.read_csv(f'{DATA_DIR}/raw.csv')
    df['age_group'] = df['age'].apply(lambda x: 'young' if x < 18 else 'adult')
    df.to_csv(f'{DATA_DIR}/processed.csv', index=False)
    print('Transform complete - processed.csv created.')
    print(df)

def load():
    df = pd.read_csv(f'{DATA_DIR}/processed.csv')
    print('Load complete - final dataset:')
    print(df)

with DAG(
    dag_id='etl_example',
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
) as dag:
    
    t1 = PythonOperator(task_id='extract_data', python_callable=extract)
    t2 = PythonOperator(task_id='transform_data', python_callable=transform)
    t3 = PythonOperator(task_id='load_data', python_callable=load)

    t1 >> t2 >> t3
