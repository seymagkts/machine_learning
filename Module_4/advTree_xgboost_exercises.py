##### XGBoost (eXtreme Gradient Boosting)

import warnings
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.model_selection import GridSearchCV, cross_validate, RandomizedSearchCV, validation_curve

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

pd.set_option("display.max_columns", None)
warnings.simplefilter(action="ignore",category=Warning)

df = pd.read_csv("diabetes.csv")

y = df.Outcome
X = df.drop(["Outcome"], axis = 1)

xgboost_model = XGBClassifier(random_state = 17).fit(X,y)

cv_results = cross_validate(xgboost_model,
                           X,
                           y,
                           cv=10,
                           scoring= ["accuracy","f1","roc_auc"]  )
print(cv_results["test_accuracy"].mean())

print(cv_results["test_f1"].mean())

print(cv_results["test_roc_auc"].mean())

print(gbm_model.get_params())

xgboost_params = {"learning_rate":[0.01,0.1],
            'max_depth': [5,8,12],
             'n_estimators': [100,500,1000],
             "colsample_bytree":[1,0.5,0.7]}

xgboost_best_grid = GridSearchCV(xgboost_model,
                             xgboost_params,
                             cv=5,
                             n_jobs=-1,
                             verbose=1).fit(X,y)

print(xgboost_best_grid.best_params_)

xgboost_final = xgboost_model.set_params(**xgboost_best_grid.best_params_,random_state = 17).fit(X,y)

cv_results = cross_validate(xgboost_final,
                           X,
                           y,
                           cv=10,
                           scoring= ["accuracy","f1","roc_auc"]  )

print(cv_results["test_accuracy"].mean())

print(cv_results["test_f1"].mean())

print(cv_results["test_roc_auc"].mean())

