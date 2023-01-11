from __future__ import print_function

import datetime
import logging

from airflow import models
from airflow.operators import bash_operator
from airflow.operators import python_operator
from airflow.operators import dummy_operator

default_dag_args = {
    'start_date': datetime.datetime(2018,1,1),
    'owner': 'airflow',
    'depends_on_past': False
}

with models.DAG(
    'ivan_simple_greeting',
    schedule_interval=datetime.timedelta(days=1),
    default_args = default_dag_args
) as dag:

    def greeting():
        logging.info('hello world')

    start = dummy_operator.DummyOperator(
        task_id = 'start',
        trigger_rule = 'all_success'
    )

    hello_python = python_operator.PythonOperator(
        task_id = 'hello',
        python_callable = greeting
    )

    goodbye_bash = bash_operator.BashOperator(
        task_id = 'goodbye',
        bash_callable = 'echo goodbye'
    )

    end = dummy_operator.DummyOperator(
        task_id = 'end',
        trigger_rule = 'all_success'        
    )

    start >> hello_python >> goodbye_bash >> end