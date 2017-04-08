
# For Loops
x = 10
counter = 0
for y in range(10 + x):
	print(y)
	print(y+1)
	counter = counter + 1

# While Loops	
counter = 0
while counter < 100:
	print(counter)
	counter = counter + 1

# If statements
if counter < 100:
	print("Less Than One Hundred")
else:
	print("Hi")

# While + nested if statements
while counter < 100:
	if counter < 60:
		print("Less Than Sixty")
	else:
		print("Greather Than Sixty")
	counter = counter + 10

# Functions
def count():
	counter = 0
	while counter < 100:
		print(counter)
		counter = counter + 1

count()

#In-class exercises
first_number = 1
second_number = 1
for i in range(20):
	next_number = first_number + second_number
	print(next_number)
	first_number = second_number
	second_number = next_number

def calculate_fib(f, s, k):
	first_number = f
	second_number = s
	for i in range(k):
		next_number = first_number + second_number
		first_number = second_number
		second_number = next_number
		print(next_number)
	return next_number

calculate_fib(1,1,20)

#NUMPY
import numpy as np











