import unittest
import pandas as pd
from sklearn.base import BaseEstimator

import sys
sys.path.append("steps")
from train import estimator_fn

class TrainTestSuite(unittest.TestCase):

    def test_type(self):
        estimator = estimator_fn()
        assert isinstance(estimator, BaseEstimator)

    def test_fit(self):
        estimator = estimator_fn()
        pdf = pd.read_csv('datasets/IRIS.csv')
        X = pdf.drop('species', axis=1)
        y = pdf.species
        estimator.fit(X, y)
        y_pred = estimator.predict(X)