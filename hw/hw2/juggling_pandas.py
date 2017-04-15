# JUGGLING PANDAS - HOMEWORK 2 AND QUIZ 2 (Below Homework 2)


#The point of this homework is to get you more practice with pandas syntax.
#There are slight differences to note here that are different from numpy so 
#do keep that in mind!

#The data set we will be using is pulled straight from Kaggle's Featured Datasets. 
#It contains 3195 records of counties with information of how "diverse" it is according 
#the the distribution of races in it for the year 2013. There are 7 different races all 
#numeric with proportions of each race in each county. Answering the tasks below will get 
#you more comfortable using pandas and its dataframe structure.

from pandas import DataFrame, Series #instead of calling pd.DataFrame every time we use it, we can just call "DataFrame"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### PROBLEM 1 ###
#Read in the csv file found in the directory of this folder, and assign it to the variable "di"

#YOUR CODE HERE








di.head()
di.shape

### PROBELM 2 ###
#Print the 42nd row and print row with label 42 (there is a differnce!)

#YOUR CODE HERE






### PROBLEM 3 ###
#Find the row that contains our county, Alameda County, CA by grabbing the Location column and comparing all its
#elements to the string "Alameda County, CA" (hint: it's di[___ == "Alameda County, CA])

#YOUR CODE HERE

#As you can see, we can select rows based on a boolean vector! Try running only the line in the middle (di[_]) to see what I mean by "boolean vector"






### PROBLEM 4 ###
#Print the counties with the maximum and minimum diversity index. Hint(when you select the column, you can attach a .min()
#right after the line to find the min of that column)

max_di = #FILL ME
min_di = #FILL ME

mm_di = di[(____________==max_di) | ________ ==min_di)]  #FILL ME (The pipe symbol "|" means "or")
mm_di


### PROBLEM 5 ###
#Make a barplot of percentages of each race for both counties you identified above (this should be a single line!)
#Also, you might want to set the legend to not appear. Look up "dataframe plot kind" in Google if you're not sure.


mm_di.iloc[,].plot() #FILL ME
plt.show()






### QUIZ PROBLEM 1 ###
#Replace all of the negative values of the following array with 0. This procedure acutally has a name!
#Look up "Rectifier (neural networks)" on wikipedia. Hint: you can do this in one line of code: consider using np.where.

import numpy as np

x = np.array([[-1, 0, 5], [23, -2, 4], [4, 2, -0.1]])

#YOUR CODE HERE




### QUIZ PROBLEM 2 ###
#Create a function that takes in a 2x2 array and calculates its determinant. This should be familiar from last week's 
#quiz. If you forgot how to calculate the determinant, look up last week's quiz!

example_array = np.array([[-2, 1], [5, 8]])

def determinant(myarray):
	determinant_value = #YOUR CODE HERE
	return determinant_value


determinant(example_array) #This should return the value -21.









