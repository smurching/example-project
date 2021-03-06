terraform {
  // TODO: MLOps team needs to supply remote state backend config here
  // otherwise CD will fail on subsequent runs
  required_providers {
    databricks = {
      source = "databrickslabs/databricks"
    }
  }
}

variable "git_repo_url" {
  type        = string
  description = "The URL of the current git repository." +
                "This variable is supplied automatically when ML resource config " +
                "is updated through automation."
}

resource "databricks_mlflow_experiment" "experiment" {
  name              = "//example-project-experiment"
  description       = "MLflow Experiment used to track runs for example-project project."
}

resource "databricks_mlflow_model" "registered_model" {
  name = "example-project Model"

  description = "My MLflow model description"
}

resource "databricks_job" "model_training_job" {
  name = "example-project model training job"

  new_cluster {
    num_workers   = 3
    spark_version = "10.5.x-cpu-ml-scala2.12"
    node_type_id  = "Standard_D3_v2"
  }

  notebook_task {
    notebook_path = "notebooks/Driver.py"
  }

  git_source {
    url = var.git_repo_url
    provider = "gitHub"
    branch = "main" # Use `master` or `main` depending on the repo's default branch.
  }

  schedule {
    quartz_cron_expression = "0 1 * * *" # daily at 1am
    timezone_id = "UTC"
  }
}

resource "databricks_job" "batch_inference_job" {
  name = "example-project batch inference job"

  new_cluster {
    num_workers   = 3
    spark_version = "10.5.x-cpu-ml-scala2.12"
    node_type_id  = "Standard_D3_v2"
  }

  notebook_task {
    notebook_path = "notebooks/BatchInference.py"
  }

  git_source {
    url = var.git_repo_url
    provider = "gitHub"
    branch = "main" # Use `master` or `main` depending on the repo's default branch.
  }

  schedule {
    quartz_cron_expression = "0 3 * * *" # daily at 3am
    timezone_id = "UTC"
  }
}

output "example-project_experiment_id" {
  value = databricks_mlflow_experiment.experiment.id
}

output "example-project_model_name" {
  value = databricks_mlflow_model.registered_model.name
}

output "example-project_training_job_id" {
  value = databricks_job.model_training_job.id
}

output "example-project_batch_inference_job_id" {
  value = databricks_job.batch_inference_job.id
}
