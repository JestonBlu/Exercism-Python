'''
Basic Python Commands
'''

## This is a list
x = [1, 2, 3, 4]
print(x)
x[0]
x[2]
x[0:3]
x[-1]


## Strings
x = "Hello"
x[1]
len(x)
x + ' World'


## This is a tuple
x = 1, 2, 3, 4
print(x)
x[3]
x[3] = 1  ## Wont work

x = (1,2,3,4),(5,6,7,8)
print(x)
x[0]
x[0][0]


## This is a dictionary
x = {'label1': 1, 'label2': 2}
print(x)
x['label1']


## This is a loop
fact = 1

## The second arguement is in range is the stopping point
for i in range(1, 3):
  fact = i
  print(fact)

## Conditional Statements
if 1 % 2 == 0:
  print('Even')
else:
  print('Odd')


## Importing Packages
import math as m
m.factorial(2)


## NumPy
## stands for Numerical Python. The most powerful feature of NumPy is
## n-dimensional array. This library also contains basic linear algebra
## functions, Fourier transforms,  advanced random number capabilities and
## tools for integration with other low level languages like Fortran, C
## and C++
##
## SciPy
## stands for Scientific Python. SciPy is built on NumPy. It is one of the
## most useful library for variety of high level science and engineering
## modules like discrete Fourier transform, Linear Algebra, Optimization
## and Sparse matrices.
##
## Matplotlib
## for plotting vast variety of graphs, starting from histograms to line
## plots to heat plots.. You can use Pylab feature in ipython notebook
## (ipython notebook –pylab = inline) to use these plotting features
## inline. If you ignore the inline option, then pylab converts ipython
## environment to an environment, very similar to Matlab. You can also use
## Latex commands to add math to your plot.
##
## Pandas
## for structured data operations and manipulations. It is extensively
## used for data munging and preparation. Pandas were added relatively
## recently to Python and have been instrumental in boosting Python’s
## usage in data scientist community.
##
## Scikit Learn
## for machine learning. Built on NumPy, SciPy and matplotlib, this
## library contains a lot of effiecient tools for machine learning and
## statistical modeling including classification, regression, clustering
## and dimensionality reduction.
##
## Statsmodels
## for statistical modeling. Statsmodels is a Python module that allows
## users to explore data, estimate statistical models, and perform
## statistical tests. An extensive list of descriptive statistics,
## statistical tests, plotting functions, and result statistics are
## available for different types of data and each estimator.
##
## Seaborn
## for statistical data visualization. Seaborn is a library for making
## attractive and informative statistical graphics in Python. It is based
## on matplotlib. Seaborn aims to make visualization a central part of
## exploring and understanding data.
##
## Bokeh
## for creating interactive plots, dashboards and data applications on
## modern web-browsers. It empowers the user to generate elegant and
## concise graphics in the style of D3.js. Moreover, it has the capability
## of high-performance interactivity over very large or streaming datasets.
##
## Blaze
## for extending the capability of Numpy and Pandas to distributed and
## streaming datasets. It can be used to access data from a multitude of
## sources including Bcolz, MongoDB, SQLAlchemy, Apache Spark, PyTables,
## etc. Together with Bokeh, Blaze can act as a very powerful tool for
## creating effective visualizations and dashboards on huge chunks of data.
##
## Scrapy
## for web crawling. It is a very useful framework for getting specific
## patterns of data. It has the capability to start at a website home url
## and then dig through web-pages within the website to gather information.
##
## SymPy
## for symbolic computation. It has wide-ranging capabilities from basic
## symbolic arithmetic to calculus, algebra, discrete mathematics and
## quantum physics. Another useful feature is the capability of formatting
## the result of the computations as LaTeX code.
##
## Requests
## for accessing the web. It works similar to the the standard python
## library urllib2 but is much easier to code. You will find subtle
## differences with urllib2 but for beginners, Requests might be more
## convenient.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../datasets/mcdonalds.csv") #Reading the dataset in a dataframe using Pandas

df.describe()
df.head()

## Count record by category
df['Category'].value_counts()

## Plots
%matplotlib inline
df['Calories'].hist(bins=10)
df.boxplot(column='Calories')

df.boxplot(column = 'Calories', by = 'Category')

df['Category'].value_counts(ascending=True)


## Count nulls
df.apply(lambda x: sum(x.isnull()), axis = 0)


import numpy as np
df['Calories_log'] = np.log(df['Calories'] + 1)
df['Calories_log'].hist(bins=20)
