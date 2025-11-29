# 2025-12-04-WEBINAR

This repository houses code and logic that will be used in the 
**Build Data Pipelines with Snowflake & Airflow | Jake McGrath** webinar hosted on 2025-12-04.

## Getting Started

1. Clone the repository using the command `None`.
2. Install the `astro` CLI. You can do this on a Mac by running `brew install astro`. For other OS's, check these docs: https://www.astronomer.io/docs/astro/cli/install-cli
3. Ensure Docker is running. You can do this by running `docker ps`.
4. Run the command `astro dev start`.
5. Navigate to `localhost:8080`.
6. Use the username `admin` and password `admin` to login.
7. Click the "Admin" icon (gear) on the left, and select "Connections".
8. Create a new Connection by clicking "Add Connection."
9. Name the connection `snowflake-retail`.
10. Select the `Snowflake` connection type, and populate the rest of the information accordingly. 
11. Trigger the `populate_bronze` DAG with the "play button". 
12. Observe the downstream execution in the `update_silver` and `update_gold` DAGs.
