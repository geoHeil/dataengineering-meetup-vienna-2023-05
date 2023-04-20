from setuptools import find_packages, setup

setup(
    name="dagster_ml_example",
    packages=find_packages(exclude=["dagster_ml_example_tests"]),
    install_requires=[
        "dagster",
        "dagster-dbt",
        "dagster_duckdb",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
