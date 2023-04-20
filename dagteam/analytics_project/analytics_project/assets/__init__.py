from dagster import asset
import pandas as pd

@asset(
    group_name = "analytics",
    compute_kind = "pandas"
)
def penguins():
    return pd.read_csv('https://gist.githubusercontent.com/slopp/ce3b90b9168f2f921784de84fa445651/raw/4ecf3041f0ed4913e7c230758733948bc561f434/penguins.csv')

