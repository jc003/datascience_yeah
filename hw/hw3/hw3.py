# HOMEWORK 3 AND QUIZ 3 (Below Homework 3)



from pandas import DataFrame, Series #instead of calling pd.DataFrame every time we use it, we can just call "DataFrame"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

### PROBLEM 1 ###
#Using the SPX data set discussed in class, fit a linear regression model on all data points.

data = pd.read_csv("FILENAME.csv", index_col=0) #FILL ME
spx = data[] #FILL ME
x = np.array([i for i in range(spx.shape[0])]) #Creating the feature column (This is the only feature column!)

clf = sm.OLS(,) #FILL ME

result = clf.fit()
result.summary()

#Using the beta coefficent found above, plot the regression line over the SPX time series plot.
#There should be two plots on one graph: 1) a time series plot like the one seen in class and 
#2) a regression line plot like the one seen in class.

#Hint: You can plot a line plot on top of another plot by calling the plt.plot function twice before plt.show!

#FILL ME (plot the spx time series here)
plt.title("GIVE A TITLE") #FILL ME
plt.xlabel("GIVE A LABEL for X AXIS") #FILL ME
plt.ylabel("GIVE A LABEL for Y AXIS") #FILL ME
plt.plot() #FILL ME (your line plot goes here)

plt.show()



### PROBLEM 2 ###
#From the line plot you created in Problem 1, do you think this line is a good "fit"? In other words,
#do you think you can use this line to predict future stock prices well? Why or why not?

#FILL ME (WRITTEN/SENTENCE ANSWER, NO CODE)






### QUIZ 3 - PROBLEM 1 ###
#A typical regression equation can be written in matrix notation as y = XB where B are your BETA coefficients.
#Given the following X and B arrays, calculate y.

import numpy as np
X = np.array([[1,1,0,0],[1,0,3,0],[1,0,0,8]])
B = np.array([[0.5],[0.3],[0.3],[0.1]])

y = #FILL ME




### QUIZ 3 - PROGBLEM 2 ###
#Now given the following y and X arrays, find the B array.

X = np.array([[1, -0.4, 2, 3.2], [1, 3, 4, -1], [1, 5, -2, 2], [1, 0, 0, 3]])
y = np.array([[2],[5],[-4],[1]])

B = #FILL ME
