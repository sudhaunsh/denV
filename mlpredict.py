import numpy as np 
# create a machine learning model using sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split    
import matplotlib.pyplot as plt

X_train = np.array([1,2,3,4,5,6,7,8,9,10,11]).reshape(-1, 1)
Y_train = np.array([155,145,110,80,62.5,50,60,80,120,175,280]).reshape(-1, 1)

clf = make_pipeline(PolynomialFeatures(3), LinearRegression())
clf.fit(X_train[:, np.newaxis], Y_train)

X_test = np.array(2).reshape(1, -1)
Y_test =  [200]
y_pred = clf.predict(X_test)
print(y_pred)