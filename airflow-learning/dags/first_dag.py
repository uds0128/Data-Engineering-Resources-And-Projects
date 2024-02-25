from datetime import datetime, timedelta

from airflow.models.dag import DAG

from airflow.operators.bash import BashOperator

with DAG(
    "first_dag",
    default_args={

    },
    description="This Is My First DAG",
    schedule=timedelta(minutes=3),
    start_date=datetime(2023,12,29),
    catchup=False,
    tags = ["veryfirstdag"]
) as dag:


    t1 = BashOperator(
        task_id = "Task12",
        bash_command='echo "Task1"',
    )

    t2 = BashOperator(
        task_id = "Task2",
        bash_command = "echo 'Task2'"
    )

    t3 = BashOperator(
        task_id = "Task3",
        bash_command = "echo 'Task3'"
    )

    t1 >> [t2,t3]
