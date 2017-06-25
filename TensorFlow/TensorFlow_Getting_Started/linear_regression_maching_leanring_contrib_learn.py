#!/usr//bin/env python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE:
#
#           USAGE:
#
#   DESCRIPTION:
#
#       OPTIONS: ----
#  REQUIREMENTS: ----
#          BUGS: ----
#         NOTES: ----
#        AUTHOR: Chyi Yaqing
#  ORGANIZATION:
#       VERSION: 0.1.0
#       CREATED: 04/24/2017
#      REVISION: ----
#      Copyright © 2017 Chyi Yaqing
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software FOundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAB PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#===================================================================
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
# Numpy if often used to load, manipulate and preprocess data
import numpy as np

# Declare list of features, we only have one real-valued feature. There are many other types of columns that are more complicated and useful
features = [tf.contrib.layers.real_valued_column("x", dimension=1)]

"""
An estimator is the front end to invoke training (fitting) and evaluation (inference).There are many predefined types like linear regression, logistic regression, linear classification, logistic classification, and many neural network classifiers and regressors.The following code provides an estimator that does linear regression.
"""
estimator = tf.contrib.learn.LinearRegressor(feature_columns=features)

"""
TensorFlow provides many helper methods to read and set up data sets,Here we use two data sets: one for training and one for evaluation we have to tell the function how many batches of data (num_epochs) we want and how big each batch should be
"""
x_train = np.array([1., 2., 3., 4.])
y_train = np.array([0., -1., -2., -3.])
x_eval = np.array([2., 5., 8., 1.])
y_eval = np.array([-1.01, -4.1, -7, 0.])
input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x_train}, y_train,batch_size=4,num_epochs=1000)
eval_input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x_eval}, y_eval, batch_size=4, num_epochs=1000)

# we can invoke 1000 training steps by invoking the method and passing the training data set
estimator.fit(input_fn=input_fn, steps=1000)

# Here we evaluate how well our model did
train_loss = estimator.evaluate(input_fn=input_fn)
eval_loss = estimator.evaluate(input_fn=eval_input_fn)
print("train loss: %r" %train_loss)
print("eval loss: %r" %eval_loss)


