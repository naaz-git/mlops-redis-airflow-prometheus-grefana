from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_local import GCSToLocalFilesystemOperator
from airflow.providers.google.cloud.operators.gcs import GCSListObjectsOperator
from airflow.operators.python import PythonOperator
from airflow.hooks.base_hook import BaseHook
from datetime import datetime
import pandas as pd
import sqlalchemy

#ETL Pipeline: CSV data extraction from Google cloud, transform and store in SQL tables using Apache Airflow
#In Industry, you will be doing reverse- means Readign SQL database then then doing data ingestion to the model pipeline

#### TRANSFORM STEP....
def load_to_sql(file_path):
    conn = BaseHook.get_connection('postgres_default')  
    engine = sqlalchemy.create_engine(f"postgresql+psycopg2://{conn.login}:{conn.password}@code_a14233-postgres-1:{conn.port}/{conn.schema}")
    df = pd.read_csv(file_path)
    df.to_sql(name="titanic", con=engine, if_exists="replace", index=False)

# Define the DAG
with DAG(
    dag_id="extract_titanic_data",
    schedule_interval=None, 
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # Extract STEP...
    list_files = GCSListObjectsOperator(
        task_id="list_files",
        bucket="mybucket-03", 
    )

    download_file = GCSToLocalFilesystemOperator(
        task_id="download_file",
        bucket="mybucket-03", 
        object_name="Titanic_Dataset.csv", 
        filename="/tmp/Titanic_Dataset.csv", 
    )
    
    ### TRANSFORM AND LOAD....
    load_data = PythonOperator(
        task_id="load_to_sql",
        python_callable=load_to_sql,
        op_kwargs={"file_path": "/tmp/Titanic_Dataset.csv"}
    )

    list_files >> download_file >> load_data
