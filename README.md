# 2025-12-04-WEBINAR

This repository houses code and logic that will be used in the 
**Build Data Pipelines with Snowflake & Airflow | Jake McGrath** webinar hosted on 2025-12-04.

## Prerequisites

In order to work through this webinar, you'll need to make sure that you have the following. You'll also need to have
an active Snowflake account/trial. The steps for setting up your Snowflake environment are also below!

- Docker installed (docs here for Mac: https://docs.docker.com/desktop/setup/install/mac-install/)
- Access to a terminal on your local machine
- Astro CLI installed. You can do this on a Mac by running `brew install astro`. For other OS's, check these docs: https://www.astronomer.io/docs/astro/cli/install-cli


### Setting Up Snowflake

1. Create a trial account or login to Snowflake. Make sure to remember your username and password.
2. Navigate to "Catalog" under Horizon Catalog.
3. Click "+ Database" in the upper-right of the screen.
4. Name the database `RETAIL`.
5. Retrieve your Snowflake "Account" identifier. This is tricky, but you'll need it when creating a Connection in Airflow. If can be found as the "Account locator". Or, if your Snowflake URL looks like this (`https://app.snowflake.com/us-east-1/tbc28388/#/data/databases`), the value would be `tbc28388`.
6. Note the name of your Snowflake Warehouse. Mine is `COMPUTE_WH`.


## Getting Started

1. Clone the repository using the command `git clone https://github.com/jroachgolf84/2025-12-04-WEBINAR.git`.
2. Run the command `astro dev start`.
3. Navigate to `localhost:8080`.
4. Use the username `admin` and password `admin` to login.
5. Click the "Admin" icon (gear) on the left, and select "Connections".
6. Create a new Connection by clicking "Add Connection."
7. Name the connection `snowflake-retail`.
8. Select the `Snowflake` connection type, and populate the rest of the information accordingly. See below for more information.
9. Turn on the `_prep` DAG. It should execute once. That's all that you'll need!


### Airflow `Connection` to Snowflake

When creating the `snowflake-retail` `Connection` in Airflow, you'll need the fields below. I've included my sample 
values as a starting point.

- `Login`: `JROACHGOLF84`
- `Password`: ...
- `Schema`: `PUBLIC`
- `Account`: `TBC28388`
- `Warehouse`: `COMPUTE_WH`
- `Database`: `RETAIL`
- `Region`: `us-east-1`
- `Role`: `ACCOUNTADMIN`
