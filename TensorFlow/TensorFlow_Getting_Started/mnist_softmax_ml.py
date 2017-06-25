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
"""
"""
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
# if you're on a Unix system simply do export TF_CPP_MIN_LOG_LEVEL=2
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# as mentioned earlier, every MNIST data point has two parts: an image of a handwritten digit and a corresponding label.
# each image is 28 pixels by 28 pixels
# Softmax Regressions -- If you want to assign probabilities to an object being one of several different things, softmax is the thing to do.The weight is negative if that pixel having a high intensity is evidence against the image being in that class, and positive if it is evidence in favor.

x = tf.placeholder(tf.float32, [None, 784]) # a value that we'll input when we ask TensorFlow to run a computation
W = tf.Variable(tf.zeros([784, 10])) # we want to multiply the 784-dimensional image vectors by it is produce 10-dimensional vectors of evidence for the difference calsses.
b = tf.Variable(tf.zeros([10])) # b has a shape of [10] so we can add it to the ouput

y = tf.nn.softmax(tf.matmul(x, W) + b)

y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.05).minimize(cross_entropy)

sess = tf.InteractiveSession()

tf.global_variables_initializer().run()

for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_:mnist.test.labels}))


