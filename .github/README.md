# CI/CD Workflow Definitions
This directory contains CI/CD workflow definitions using [GitHub Actions](https://docs.github.com/en/actions),
under ``workflows``. These workflows cover testing and deployment of
both ML code (for model training, batch inference, etc) and the 
Databricks ML resource definitions under ``databricks-config``.
 
## Configuring secrets
The included CI/CD worfklows depend on the secrets listed below. By default,
the workflows read secrets values from
[GitHub Actions Encrypted Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets), but
you can modify them to read secrets from elsewhere. 

* Credentials for Databricks authentication:* DEV_WORKSPACE_TOKEN
  * STAGING_WORKSPACE_TOKEN
  * PROD_WORKSPACE_TOKEN

The exact steps are described [in these docs](https://github.com/databricks/run-notebook/blob/main/README.md#prerequisites)
for the ``run-notebook`` GitHub Action used to drive CI/CD in the workflows under `.github`.