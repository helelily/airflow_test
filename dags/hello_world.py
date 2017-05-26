from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

DEFAULT_ARGS = {"owner" : "theflow",
		"depends_on_past" : False,
		"start_date" : datetime(2017,05,26,16,30),
		"retries" : 1,
		"retry_delay" : timedelta(minutes=1)}
SCHEDULE_INTERVAL = "@once"

dag = DAG("hello_world",
	  default_args=DEFAULT_ARGS,
	  schedule_interval=SCHEDULE_INTERVAL)

demo_task = BashOperator(
	task_id="hello_world_command",
	bash_command="echo \"Hello World!\"",
	dag=dag
)
