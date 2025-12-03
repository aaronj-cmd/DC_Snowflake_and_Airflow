from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

from datetime import datetime

from include.loader import load_table


with DAG(
    dag_id="_prep",
    start_date=datetime(2025, 1, 1),
    schedule="@once"
) as dag:

    _load_album_table = PythonOperator(
        task_id="load_album_table",
        python_callable=load_table,
        op_kwargs={
            "data_file_name": "Album.csv",
            "ddl_file_name": "album.sql",
            "table_name": "album",
            "snowflake_conn_id": "snowflake-retail"
        }
    )

    _load_artist_table = PythonOperator(
        task_id="load_artist_table",
        python_callable=load_table,
        op_kwargs={
            "data_file_name": "Artist.csv",
            "ddl_file_name": "artist.sql",
            "table_name": "artist",
            "snowflake_conn_id": "snowflake-retail"
        }
    )

    _load_invoice_table = PythonOperator(
        task_id="load_invoice_table",
        python_callable=load_table,
        op_kwargs={
            "data_file_name": "Invoice.csv",
            "ddl_file_name": "invoice.sql",
            "table_name": "invoice",
            "snowflake_conn_id": "snowflake-retail"
        }
    )

    _load_invoice_line_table = PythonOperator(
        task_id="load_invoice_line_table",
        python_callable=load_table,
        op_kwargs={
            "data_file_name": "InvoiceLine.csv",
            "ddl_file_name": "invoice_line.sql",
            "table_name": "invoice_line",
            "snowflake_conn_id": "snowflake-retail"
        }
    )

    _load_track_table = PythonOperator(
        task_id="load_track_table",
        python_callable=load_table,
        op_kwargs={
            "data_file_name": "Track.csv",
            "ddl_file_name": "track.sql",
            "table_name": "track",
            "snowflake_conn_id": "snowflake-retail"
        }
    )

    # Run all Tasks in parallel
    [
        _load_album_table,
        _load_artist_table,
        _load_invoice_table,
        _load_invoice_line_table,
        _load_track_table
    ]
