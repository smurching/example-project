walgreens
==============================

This directory contains an ML project based on the
[Databricks MLOps Project Template](https://github.com/databricks/mlops-project-template).


## Project Structure
```
├── README.md          <- README for developers using this project
│
├── steps              <- Python modules implementing ML pipeline logic, e.g. model training and evaluation
│
├── notebooks          <- Databricks notebooks that call into the pipeline step modules under `steps`. Used to
│                         drive code execution on Databricks for CI/CD. See comments at top of each notebook
│                         for details on expected interface of the notebook
│
├── .github            <- Configuration folder for CI/CD using GitHub Actions. The CI/CD workflows run the notebooks
│                         under `notebooks` to test and deploy model training code
│
├── databricks-config  <- ML resource (ML jobs, MLflow models) config definitions expressed as code, across dev/staging/prod
│   ├── dev
│   ├── staging
│   ├── prod
│
├── requirements.txt   <- Specifies Python dependencies for ML code (model training, batch inference, etc) 
│
├── tests              <- Tests for the modules under `steps`
```

## Getting Started
Data scientists can get started right away iterating on and testing ML code under ``steps``. Interactively edit
and run the code in your IDE or on Databricks using [Repos](https://docs.databricks.com/repos/index.html).

## Productionizing your ML Project
After you've explored and validated the ML problem at hand, you may be ready to start productionizing your ML pipeline.
The first step is to submit a PR with your ML code changes. At this point, you (or your IT/ops team) must:

1. Configure appropriate secrets in GitHub Actions for triggering notebook execution in CI & CD. See the README under `.github` for details.
2. Set up terraform remote state storage for deploying ML resource configuration. See the README under `databricks-config` for details
