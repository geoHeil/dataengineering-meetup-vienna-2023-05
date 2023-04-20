from setuptools import find_packages, setup

setup(
    name="ml_project",
    packages=find_packages(exclude=["ml_project_tests"]),
    install_requires=[
        "dagster",
        "pandas",
        "scikit-learn",
        "dagster-cloud",
        "boto3"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
