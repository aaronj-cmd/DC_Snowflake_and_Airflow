from airflow.sdk import DAG, Asset
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

from datetime import datetime

# Define your query!
is_greatest_hits_query: str = """____"""

with DAG(
        dag_id="update_silver",
        start_date=datetime(2025, 1, 1),
        schedule=[
            Asset("bronze_album"),
            Asset("bronze_artist"),
            Asset("bronze_invoice"),
            Asset("____"),
            Asset("____")
        ],
        template_searchpath="include/sql"  # Where to look for SQL queries
) as dag:

    curate_greatest_hits = SQLExecuteQueryOperator(
        task_id="curate_greatest_hits",
        conn_id="snowflake-retail",
        sql=is_greatest_hits_query,
        outlets=[Asset("silver_greatest_hits")],
    )

    build_detailed_invoices = SQLExecuteQueryOperator(
        task_id="build_detailed_invoices",
        conn_id="____",
        sql="____.sql",  # Build the invoice using a query in include/sql
        outlets=[Asset("____")]  # "Outlet" to the silver_detailed_invoices Asset
    )

    # Execute the Tasks in parallel
    [None, None]
