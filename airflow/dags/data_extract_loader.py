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
import db_utilimport os
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