# JUGGLING PANDAS - HOMEWORK 2


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
#Also, you might want to set the legend to not appear. Look up "dataframe plot kind" in Google  if you're not sure.


mm_di.iloc[,].plot() #FILL ME
plt.show()





