###################### POKEMON GO CLOSEST SPAWN POINT ########################################
#The goal of this assignment is to get you wrangling with numpy and data. In general, 
#you will be using pandas for 90% of your data analysis needs but for the other 10%,
#numpy is still used. This first task is one of them (okay, you can actually do most of
#this in pandas but it's still very good to know how to do with numpy:)).

#Below is a file that contains latitude and longitude coordinates of Pokemon spawn
#locations in UC Berkeley's campus. Each spawn location spawns a certain pokemon at a
#particular time each hour according to some distribution. Naturally, standing in a spot
#with multiple spawn points close to one another would increase the rate of Pokemon to catch.
#Your second task is to plot these points to get a general sense of how the spawnpoints are
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

# PROBLEM 3 - Find closest two spawn points
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

# PROBLEMS 4-6 - Image Convolution
#Images are often stored as an n x n matrix. This problem will have you read in sample
#image data on handwritten numbers 0,1,2,3,4,5,6,7,8,9, as well as perform an operation
#called a "convolution". To read more about how convolution works, visit:
#http://cs231n.github.io/convolutional-networks/
#And scroll down to "Convolution Demo" under the Convolution Layer section. They show
#a visual demonstration of convolving with a 3x3 matrix filter at a stride of 2 (e.g. the
#filter is moved to the right two steps instead of one). Don't worry about the fancy
#topics from the other sections. The purpose of this problem is to show you that very
#complicated techniques can be done with simple numpy array operations (and for loops).

#For those curious, this particular convolution procedure is used to train a machine
#learning model called a Neural Network. Neural networks are designed to behave much
#like the human brain and is able "learn" things based on what it sees. The convolution
#step is one out of many steps to build up this kind of model but it just so happens
#that this step only requires matrix multiplication and/or array indexing.

# PROBLEM 4 - Read in the image data
data = np.loadtxt("FILL ME", delimiter=",") #Fill in the file name of your data

# PROBLEM 5 - Visualize the first number
#Your data array is 10 x (784 + 1). The last column is the label of the number that is
#represented in each row. For example, row 0 is the digit 5. Notice that each image
#has been "flattened" down to a vector of 1 x 784. To actually visuzlize this number
#we need to "reshape" it into a 28x28 array that we are more familiar with. First
#select the first row but excluding the label column.

img = #FILL ME

#Next reshape the image vector

img_reshaped = np.reshape(img, ) #FILL ME

#Finally we can visualize the image with plt's imshow function.

plt.imshow() #FILL ME
plt.show()

# PROBLEM 6 - Convolving
#This problem is open-eneded since there are a couple of ways of doing this. Unlike
#the demo from the link I gave you above, you are required to convolve with a stride of
#1 and NO ZERO PADDING is necessary. Your task is to convolve on only the first image
#(the one your visualized in the last problem). The output should be a 26x26 array.

#Please use this filter kernel to use as you convolve:
kernel = np.ones((3,3))

#hint: the most intuitive method is to use a couple of for loops (my solution has 4).

#FILL ME


#Once you are done with this assignment, please email this file to jerryc@berkeley.edu.
#Please put [Yeah-HW1] <First Name> <Last Name> as the subject header!
#Homework 1 is due 4/15 9:30am.




