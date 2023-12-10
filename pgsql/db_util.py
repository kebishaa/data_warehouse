import sys
import pandas as pd
from sqlalchemy import text
import json
from sqlalchemy import create_engine
import numpy as np

# engine = create_engine('postgresql+psycopg2://airflow:airflow@192.168.1.100:8585/postgres')
engine = create_engine('postgresql+psycopg2://airflow:airflow@host.docker.internal:8585/postgres')

VEHICLE_SCHEMA = "timed_vehicle_data_schema.sql"
TRAJECTORIES_SCHEMA = "trajectory_schema.sql"


def create_table():
    try:
        with engine.connect() as conn:
            for name in [TRAJECTORIES_SCHEMA,VEHICLE_SCHEMA]:
                
                with open(f'/opt/pgsql/{name}', "r") as file:
                    query = text(file.read())
                    conn.execute(query)
        print("Successfull")
    except Exception as e:
        print("Error creating table",e)
        sys.exit(e)
