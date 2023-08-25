
#Libraries used are NumPy,Pandas,MatPlotLib

#NumPy can be used for numerical and mathematical operations. 
#It provides support for multi-dimensional arrays.

#Pandas can be used forpowerful data manipulation and analysis library in Python. 
#It provides data structures and functions for working with structured data. 

#MatPlotLib can be used for Graphical representations of data
#It creates static, animated, and interactive visualizations in figures, plots, charts, and graphs

#NumPy is used in these code for creating an array to store dataset of House Size(in square feet) and House Price(in thousands).
#Pandas is used in these code for creating dataframe to represent dataset in terminal in tabular form.
#MatPlotLib is used in these code for creating a graph that is visual representaion of dataset.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x=np.array([1,2,3,4,5])
y=np.array([300,500,700,900,1100])

#Coverting the numpy aray into pandas dataframe 
df1 = pd.DataFrame(x, columns = ['Size'])
df2 = pd.DataFrame(y, columns = ['Price'])
print(df1)
print(df2)

#Matplotlib Graph
print(f"x={x}")
print(f"y={y}")
# output -> x=[1 2] y=[300 500]

# m-> number of training data sets
m=x.shape[0]
print(f"Number of points: {m}")

i=0
x_i=x[i]
y_i=y[i]
print(f"(x^({i}), y^({i})) = ({x_i}, {y_i})")
#Plotting data
#You can plot these two points using the scatter() function 
#The function arguments marker and c show the points as red crosses
plt.scatter(x,y,marker='x',c='r')
# set title
plt.title("Housing price")
#set axis label
plt.ylabel("Price")
plt.xlabel("Size")

plt.show()


