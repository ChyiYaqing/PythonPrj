#!/usr/bin/env python3

import pandas as pd # read our data set.
from sklearn import linear_model # machine leanring library
import matplotlib.pyplot as plt # visualize our model and data

#read data
dataframe = pd.read_fwf('brain_body.txt') # fwf fixed width formatted lines
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

#train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

#visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()
