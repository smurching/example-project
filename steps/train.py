def estimator_fn():
  from sklearn.svm import SVC
  from sklearn.model_selection import GridSearchCV
  estimator = SVC()
  parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
  estimator = GridSearchCV(estimator, parameters)

  return estimator