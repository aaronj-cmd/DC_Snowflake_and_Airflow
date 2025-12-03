from airflow.sdk import DAG, Asset
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


with DAG(
    dag_id="SOLUTION_update_gold",
    schedule=[Asset("silver_greatest_hits"), Asset("silver_detailed_invoice")],
    template_searchpath="include/sql"
) as dag:

    update_greatest_hits_sales = SQLExecuteQueryOperator(
        task_id="update_greatest_hits_sales",
        conn_id="snowflake-retail",
        sql="gold_greatest_hits_sales.sql",
        outlets=[Asset("gold_greatest_hits_sales")]
    )
