#Once you are done with this quiz, simply save this file and send to my email address at: jerryc@berkeley.edu
#Please put [Yeah-Quiz] <First Name> <Last Name> as the subject header!
#The quiz is due at the same time as your homework: 4/15 9:30am.

######################################################################
#Name: Bob Smith (REPLACE WITH YOUR FULL NAME)

#Question 1
#Find the maximum value of the following list using 1) the np.max function and 2) without the np.max function

q1 = [1, 0, -10, 11, 2, 7, 5]

import numpy as np
np.max(q1) #FILL ME

#FILL ME
holder = 0
for i in range(7):
	val = q1[i]
	if val > holder:
		holder = val

print(holder)


#Question 2
#Print the numbers 1 to 100 with a for loop. If the number is divisible by 7 print "pop". If the number
#is divisble by 11 print "corn". 

#FILL ME
for i in range(1,101):
	to_print = i
	if i % 7 == 0:
		to_print = "pop"
	if i % 11 == 0:
		to_print = "corn"
	print(to_print)



#Question 3
#Calculate the determinant of the following matrix without the np.linalg.det function.
#The determinant of a 2x2 matrix is: http://www.purplemath.com/modules/determs.htm
#You should NOT type "4*3 - 1*2". Subset the array with index notation like mat[0,0] to get the values.

mat = np.array([[4,1],[2,3]])
#FILL ME

det = mat[0,0] * mat[1,1] - mat[1,0] * mat[0,1]
print(det)


