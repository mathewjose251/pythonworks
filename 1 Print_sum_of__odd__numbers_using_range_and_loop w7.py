#This Program is a sample program
#Modellling for loop
# using range function
# What is range ?
#range() generates the integer numbers between the given start integer to the stop integer, i.e., It returns a range object.
# Using for loop, we can iterate over a sequence of numbers produced by the range() function
# range() function syntax and arguments
# range(start, stop[, step])
# It takes three arguments. Out of the three 2 arguments are optional.
# I.e., start and step are the optional arguments.
#
# A start argument is a starting number of the sequence. i.e., lower limit.
# By default, it starts with 0 if not specified.
# A stop argument is an upper limit. i.e., generate numbers up to this number,
# The range() doesn’t include this number in the result.
# The step is a difference between each number in the result.
# The default value of the step is 1 if not specified.
# so no we know what is teh use of range function
# for our program how can we use range() function ?
# we need only odd numbers ===>> Means we can start range ( start value as 1, Stop value,Step value as 2)
# lets try checking it , if i want to print odd numbers from 1 to 10 , I can use range as below ,with a for loop.
for number in range (1,10,2):
    print ("The current number is " ,number)

#Work for Avyu
#print the even numbers using the above program logic
#please write a new program like this

