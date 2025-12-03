from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook

import os

# Airflow home path
AIRFLOW_HOME = os.getenv("AIRFLOW_HOME", "/usr/local/airflow")


def load_table(data_file_name, ddl_file_name, snowflake_conn_id, table_name):
    with open(f"{AIRFLOW_HOME}/include/data/DDL/{ddl_file_name}", "r") as ddl_file:
        ddl = ddl_file.read()

    # Create the cursor used to execute statements
    snowflake_hook = SnowflakeHook(snowflake_conn_id=snowflake_conn_id)
    snowflake_conn = snowflake_hook.get_conn()
    snowflake_cursor = snowflake_conn.cursor()

    # Run the DDL
    snowflake_cursor.execute(ddl)

    # Add the file to internal stage
    snowflake_cursor.execute(f"PUT file://{AIRFLOW_HOME}/include/data/{data_file_name} @%{table_name}")

    # Load the file into the table
    snowflake_cursor.execute(f"""
        COPY INTO {table_name}
        FROM @%{table_name}
        FILE_FORMAT = (TYPE = CSV SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY='\"')
    """)

    snowflake_conn.commit()
