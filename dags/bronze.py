from airflow.sdk import DAG, task, Asset

from datetime import datetime


with DAG(
    dag_id="populate_bronze",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
) as dag:

    @task(outlets=[Asset("bronze_album")])
    def album():
        print("Populating bronze_album table.")

    @task(outlets=[Asset("bronze_artist")])
    def artist():
        print("Populating bronze_artist table.")

    @task(outlets=[Asset("bronze_invoice")])
    def invoice():
        print("Populating bronze_invoice table.")

    @task(outlets=[Asset("bronze_invoice_lines")])
    def invoice_lines():
        print("Populating bronze_invoice_lines table.")


    @task(outlets=[Asset("bronze_track")])
    def track():
        print("Populating bronze_track table.")

    # Execute the Tasks
    [
        album(),
        artist(),
        invoice(),
        invoice_lines(),
        track()
    ]
