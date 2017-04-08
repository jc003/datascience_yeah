###################### POKEMON GO CLOSEST SPAWN POINT ##################################
#The goal of this assignment is to get you wrangling with numpy and data. In general, 
#you will be using pandas for 90% of your data analysis needs but for the other 10%,
#numpy is still used. This task is one of them (okay, you can actually do most of this)
#in pandas but it's still very good to know how to do with numpy:)).

#Below is a file that contains latitude and longitude coordinates of spawn locations in
#UC Berkeley's campus. Each spawn locatio spawns a certain pokemon at a particular time
#each hour according to some distribution. Naturally, standing in a spot with multiple
#spawn points close to one another would increase the rate of Pokemon to catch. Your
#second task is to plot these points to get a general sense of how the spawnpoints are
#scattered.

import numpy as np
import matplotlib.pyplot as plt

# PROBLEM 1 - Reading in the data
spawns = np.loadtxt("FILL ME", delimiter=",") #Fill in the file name of your data

# PROBLEM 2 - Create a scatterplot
#Each row in variable spawns corresponds to a unique Pokemon spawn point. The first
#column is latitude and the second column is longitude. Make a scatter plot of these
#spawn locations. You will need to subset the spawns array appropriately. If you are
#unsure of what to put inside the plotting function, look the function up on Google:)

plt.scatter() #FILL ME
plt.show() #Calls the show function to show the plot in a new window

#FILL ME

#PROBLEM 3 - Find closest two spawn points
#It would be great if we can identify a spot in Berkeley that has the densest cluster
#of spawn points. Identify the two spawn points that are closest to each other out of
#all spawn points. The distance between two points can be defined in many ways. I 
#recommend you use the euclidean distance. An example of euclidean distance is 
#given below:

vector1 = np.array([1,1])
vector2 = np.array([0,0])
distance = np.sqrt(np.sum((vector1 - vector2)**2)) #This is equal to the square root of 2

#I have given you some skeleton code to help with this part of the assignment:

dist_array = np.zeros((spawns.shape[0],spawns.shape[0])) #Initializes the distance array
for i in range(len(spawns)):
	for j in range(len(spawns)):
		dist_array[i,j] = #FILL ME

#Next find out the i,j index for the minimum distance value in the dist_array matrix.
#You might find the functions np.where and np.min useful.
# FILL ME

#Use the i,j index to select the two spawn points that are closest to each other in
#the variable spawns.
# FILL ME

#Once you are done with this assignment, please email this file to jerryc@berkeley.edu.
#Please put [Yeah-HW1] <First Name> <Last Name> as the subject header!
#Homework 1 is due 4/15 9:30am.