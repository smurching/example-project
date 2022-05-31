import unittest
import pandas as pd
from sklearn.pipeline import Pipeline

import sys
sys.path.append("steps")
from transform import transformer_fn

class TrainTestSuite(unittest.TestCase):

    def test_type(self):
        transformer = transformer_fn()
        assert isinstance(transformer, Pipeline)

    def test_fit(self):
        transformer = transformer_fn()
        pdf = pd.read_csv('datasets/IRIS.csv')
        X = pdf.drop('species', axis=1)
        y = pdf.species
        transformer.fit(X, y)