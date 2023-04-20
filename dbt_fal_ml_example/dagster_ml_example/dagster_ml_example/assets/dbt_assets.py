
from dagster._utils import file_relative_path
from dagster_dbt import load_assets_from_dbt_project

DBT_PROJECT_DIR = file_relative_path(__file__, "../../../dbt/")
DBT_PROFILES_DIR = file_relative_path(__file__, "../../../dbt/config")

assets = load_assets_from_dbt_project(
    DBT_PROJECT_DIR,
    #DBT_PROFILES_DIR,
    key_prefix=["ml"],
    io_manager_key="io_manager",
    select="customer_orders_labeled customer_orders"
)