from airflow.sdk import DAG, Asset
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

from datetime import datetime

# Define your query!
is_greatest_hits_query: str = """
    CREATE OR REPLACE VIEW silver_greatest_hits AS (
        SELECT
            album.albumid, 
            album.title AS album_name, 
            artist.name AS artist_name,

            -- Determine if an album is a "Greatest Hits" album
            CASE 
                WHEN album_name ILIKE '%greatest%' THEN TRUE
                ELSE FALSE
            END AS is_greatest_hits

        FROM album
        JOIN artist ON album.artistid = artist.artistid
    );
"""

with DAG(
        dag_id="update_silver",
        start_date=datetime(2025, 1, 1),
        schedule=[
            Asset("bronze_album"),
            Asset("bronze_artist"),
            Asset("bronze_invoice"),
            Asset("bronze_invoice_lines"),
            Asset("bronze_track")
        ],
        template_searchpath="include/sql"  # Where to look for SQL queries
) as dag:

    curate_greatest_hits = SQLExecuteQueryOperator(
        task_id="curate_greatest_hits",
        conn_id="snowflake-retail",
        sql=is_greatest_hits_query,
        outlets=[Asset("silver_greatest_hits")],
    )

    build_detailed_invoice = SQLExecuteQueryOperator(
        task_id="build_detailed_invoice",
        conn_id="snowflake-retail",
        sql="build_invoice.sql",
        outlets=[Asset("silver_detailed_invoice")]
    )

    [curate_greatest_hits, build_detailed_invoice]
