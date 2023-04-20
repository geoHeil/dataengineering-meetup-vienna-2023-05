# Data engineering meetup vienna

- 2023-05-10
- https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7053697508119584769/

Georg Heiler will be talking about the Modern Data Stack in the Enterprise, describing the Data Platform at Magenta Telekom, a deep dive into their tech stack and a comparison between #Dagster & #Airflow for their business needs.

## follow along

### prerequisites

- mambaforge https://mamba.readthedocs.io/en/latest/installation.html
- make
- git
- a text editor (VSCode?)

### setup

```bash
make create_environment
# on ARM/apple silicon use for a rosetta based build - unfortunately, still not all packages do support ARM
make create_environment_osx

make case1-dagteam
make case2-dbt-fal-dagster
make case3-hoolie
```

The 3 examples are based on:

- https://github.com/slopp/dagteam
- https://github.com/fal-ai/dbt_fal_ml_example and https://blog.fal.ai/build-and-deploy-machine-learning-models-from-jupyter-notebooks-with-fal-and-dbt/. 
    - this is an adaptation to dagster
    - and a nice connection to the previous talk
- https://github.com/dagster-io/hooli-data-eng-pipelines