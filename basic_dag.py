from __future__ import print_function
import datetime
from airflow import models
from airflow.operators import bash_operator
from airflow.operators import python_operator
from airflow.operators import dummy_operator

default_dag_args = {
    'start_date': datetime.datetime(2018,1,1)
}

with models.DAG(
    'ivan_simple_greeting',
    schedule_interval=datetime.timedelta(days=1),
    default_dag_args = default_dag_args) as dag;
