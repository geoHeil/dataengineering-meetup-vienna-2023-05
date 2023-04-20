# ml_project

This is a [Dagster](https://dagster.io/) project scaffolded with [`dagster project scaffold`](https://docs.dagster.io/getting-started/create-new-project). 

The project is scoped to the ML team and has its own dependencies.

## Getting started

```bash
source .venv-mlproject/bin/activate
pip install -e ".[dev]"
```

Then, start the Dagit web server:

```bash
dagit
```

Open http://localhost:3000 with your browser to see the project.

You can start writing assets in `analytics_project/assets/`. The assets are automatically loaded into the Dagster repository as you define them.

