# linear_regression_demo
This is the code for "How to Make a Prediction - Intro to Deep Learning #1' by Siraj Raval on YouTube

##Overview
This is the code for [this](https://youtu.be/vOppzHpvTiQ) video by Siraj Raval on Youtube. This is the 1st episode in my 'Intro to Deep Learning' series. The goal is to predict an animal's body weight given it's brain weight. The model we'll be using is called [Linear Regression](http://www.statisticssolutions.com/what-is-linear-regression/). The dataset we're using to train our model is a list of brain weight and body weight measurements from a bunch of animals. We'll fit our line to the data
using the scikit learn machine learning library, then plot our graph using matplotlib.Traditionary, programming has been about defining single step for a program to reach an outcome. The machine learning is about defining the outcome, and our program will learn the steps to get there.

And you know that rule that says you need 10,000 hours to master any skill  "Neural Network" -- When you use a neural network that's not just one or two, but many layers deep to make a prediction, we call that deep learning. It's a subset of machine learning that has outperformed. We usually class learning into three different styles:
    -- supervised learning 监督学习-- it just have to learn the mapping between the labels and data.
    -- Unsupervised Learning 非监督学习 -- this is when we give a model a data set without labels.It's gets no feedback on what's correct or not.It has to learn by itself.
    -- Reinforcement learning 增强学习 --  

##Dependencies

* pandas
* scikit-learn
* matplotlib

You can just run
`pip install -r requirements.txt` 
in terminal to install the necessary dependencies. Here is a link to [pip](https://pip.pypa.io/en/stable/installing/) if you don't already have it.

##Usage

Type `python demo.py` into terminal and you'll see the scatter plot and line of best fit appear.

##Challenge

The challenge for this video is to use scikit-learn to create a line of best fit for the included 'challenge_dataset'. Then, make a prediction for an existing data point and see how close it matches up to the actual value. Print out the error you get. You can use scikit-learn's [documentation](http://scikit-learn.org/stable/documentation.html) for more help. These weekly challenges are not related to the Udacity nanodegree projects, those are additional.

*Bonus points if you perform linear regression on a dataset with 3 different variables*

##Credits

The credits for the original code go to [gcrowder](https://github.com/gcrowder). I've merely created a wrapper to get people started.

