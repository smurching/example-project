# Databricks ML Resource Config
This directory includes Databricks ML resource configuration, i.e. the definitions of a batch
inference job, a training job, an MLflow experiment, and an MLflow model.
Configurations are split into separate `dev/main.tf`, `staging/main.tf`, and `prod/main.tf` files
for separate environments, and are expressed in the [Terraform language](https://www.terraform.io/language#terraform-language-documentation). 

## Prerequisite: configure remote state storage
Note: this one-time setup step is typically done by ops teams.

To enable usage of the config interface, you must first configure a [remote terraform backend](https://www.terraform.io/language/settings/backends) for storing the state of
deployed resources. Then, update `dev/main.tf`, `staging/main.tf`, and `prod/main.tf` to specify
an appropriate remote backend. 

 
## Develop and test config changes
To get started, open `dev/main.tf`.  The file contains ML resource definitions, like

```$xslt
resource "databricks_job" "batch_inference_job" {
  name = "My ML project batch inference job"

  new_cluster {
    num_workers   = 3
    spark_version = "10.5.x-cpu-ml-scala2.12"
    node_type_id  = "Standard_D3_v2"
  }

  notebook_task {
    notebook_path = "notebooks/BatchInference.py"
  }
  ...
}
```

The example above defines a Databricks job with name `My ML project batch inference job`
that runs the notebook under `notebooks/BatchInference.py` to regularly apply your ML model
for batch inference. 

At the start of the resource definition, we specify its type (`databricks_job`)
and assign it the local name ``batch_inference_job``. The local name is a variable
name that allows referencing the job within the same ``main.tf`` file, but has no bearing
on the job's name in Databricks.

To test out a config change, simply edit one of the fields above, e.g. 
increase cluster size by bumping `num_workers` from 3 to 4. 
The list of supported fields and additional examples for all Databricks resources can be found in the 
[Databricks Terraform Provider docs](https://registry.terraform.io/providers/databrickslabs/databricks/latest/docs/resources/job).
In general, the field names and types match those provided by the Databricks REST API.

You can then open a pull request (PR). Continuous integration will automatically update the dev Databricks workspace
with the config changes from your PR. Note that changes to `staging/main.tf` and `prod/main.tf` are not automatically deployed from PRs, but instead
will be deployed once your PR is approved and merged. Once your changes to dev are deployed, log into the dev
workspace and verify that they look good.

In this example, we walked through modifying an attribute of an existing resource, i.e. increasing the
size of a job cluster. You can also add or remove resource blocks to create or delete ML resources,
for example to enable or disable model monitoring.

### See also
* [Databricks Terraform Provider docs](https://registry.terraform.io/providers/databrickslabs/databricks/latest/docs/resources/job) for the supported fields and additional examples for Databricks resources
* Official docs on [Terraform resource syntax](https://www.terraform.io/language/resources/syntax#resource-syntax)

## Deploy config changes

Once you've tested your config changes in dev and are ready to deploy them to a pre-production or production
environment, you can submit a pull request (PR) updating the `main.tf` files, e.g. `staging/main.tf` and
`prod/main.tf` . In general, we recommend keeping staging and prod consistent, so most PRs should update both files.

When your PR merges, continuous deployment automation will deploy changes to staging and then prod.
