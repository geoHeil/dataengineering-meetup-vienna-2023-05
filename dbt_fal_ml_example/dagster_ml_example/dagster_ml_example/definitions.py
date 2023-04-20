import os
from dagster import (
    Definitions,
    load_assets_from_modules,
    load_assets_from_package_module,
    fs_io_manager,
)
from dagster_duckdb import build_duckdb_io_manager
from dagster_duckdb_pandas import DuckDBPandasTypeHandler
from dagstermill import local_output_notebook_io_manager

from .assets import dbt_assets
from .assets.dbt_assets import DBT_PROJECT_DIR, DBT_PROFILES_DIR
from . import ml_assets
from dagster_dbt import dbt_cli_resource

dbt_assets = load_assets_from_modules([dbt_assets])

# Our final set of assets represent Python code that
# should run after dbt.
#!!! TODO enable
ml_assets = load_assets_from_package_module(
    ml_assets,
    group_name="FORECASTING"
)


def get_env():
    # for sake of simplicity only local is supported
    return "LOCAL"

# Locally, have dagster use DuckDB as the database
# See dbt/config/profiles.yml to see the matching dbt config
duckdb_io_manager = build_duckdb_io_manager([DuckDBPandasTypeHandler()]).configured(
    {"database": os.path.join(DBT_PROJECT_DIR, "dbt_ml.duckdb")}
)

# Similar to having different dbt targets, here we create the resource
# configuration by environment
resource_def = {
    "LOCAL": {
        "io_manager": duckdb_io_manager,
        "model_io_manager": fs_io_manager,
        "output_notebook_io_manager": local_output_notebook_io_manager,
        "dbt": dbt_cli_resource.configured({
            "project_dir": DBT_PROJECT_DIR,
            "profiles_dir": DBT_PROFILES_DIR,
            "target": "LOCAL"
        }),
    },
}

defs = Definitions(
    assets = [*dbt_assets, 
              *ml_assets
              ],
    resources = resource_def[get_env()]
)
