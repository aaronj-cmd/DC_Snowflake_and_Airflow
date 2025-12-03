from airflow.sdk import DAG, Asset
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


with DAG(
    dag_id="update_gold",
    # Trigger when silver_greatest_hits and silver_detailed_invoices Assets are updated
    schedule=[Asset("____"), Asset("____")],
    template_searchpath="____"  # Read sql files from include/sql
) as dag:

    update_greatest_hits_sales = SQLExecuteQueryOperator(
        task_id="update_greatest_hits_sales",
        conn_id="____",  # Snowflake connection
        sql="____.sql",  # Run the correct query from include/sql
        outlets=[Asset("gold_greatest_hits_sales")]
    )
