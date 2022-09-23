import os
import sys
from datetime import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

cwd=os.getcwd()
sys.path.append(f'../scripts/')
sys.path.append(f'../pgsql/')
sys.path.append(f'../temp_storage/')
sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)))
from extractor import DataExtractor
import db_utilimport
import sys
from datetime import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

cwd=os.getcwd()
sys.path.append(f'../scripts/')
sys.path.append(f'../pgsql/')
sys.path.append(f'../temp_storage/')
sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)))
from extractor import DataExtractor
import db_util

data_extractor=DataExtractor()

def extract_data(ti):

    loaded_df_name=data_extractor.extract_data(file_name='20181024_d1_0830_0900.csv',return_json=True)
    trajectory_file_name,vehicle_file_name=loaded_df_name
   
    ti.xcom_push(key="trajectory",value=trajectory_file_name)
    ti.xcom_push(key="vehicle",value=vehicle_file_name)
def create_table():
    db_util.create_table()

def populate_table(ti):
    trajectory_file_name = ti.xcom_pull(key="trajectory",task_ids='extract_from_file')
    vehicle_file_name = ti.xcom_pull(key="vehicle",task_ids='extract_from_file')
    # trajectory_data,vehicle_data=combined_df['trajectory'], combined_df['vehicle']
    db_util.insert_to_table(trajectory_file_name, 'trajectories',from_file=True)
    db_util.insert_to_table(vehicle_file_name, 'vehicles',from_file=True)

def clear_memory(ti):
    trajectory_file_name = ti.xcom_pull(key="trajectory",task_ids='extract_from_file')
    vehicle_file_name = ti.xcom_pull(key="vehicle",task_ids='extract_from_file')

    os.remove(f'../temp_storage/{trajectory_file_name}')
    os.remove(f'../temp_storage/{vehicle_file_name}')
