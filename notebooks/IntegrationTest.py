# Databricks notebook source

# This notebook has no input nor output. It runs some integration tests to verify model training
# succeeds using code from the current branch.
import sys
sys.path.append("../steps")

# COMMAND ----------

from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
import pandas as pd

from train import estimator_fn
from transform import transformer_fn

# COMMAND ----------

import mlflow
from mlflow.tracking import MlflowClient
client = MlflowClient()
model_name = "ML Model Test"
mlflow.set_experiment("//walgreens-experiment")

# COMMAND ----------

pdf = pd.read_csv('../datasets/IRIS.csv')
X = pdf.drop('species', axis=1)
y = pdf.species
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=9)

mlflow.sklearn.autolog(log_input_examples=True, silent=True)
estimator = estimator_fn()
transformers = transformer_fn()
pipeline = make_pipeline(
  transformers,
  estimator
)

with mlflow.start_run() as run:
    pipeline.fit(X_train, y_train)
    # log test metrics
    mlflow.sklearn.eval_and_log_metrics(pipeline, X_test, y_test, prefix="test_")
