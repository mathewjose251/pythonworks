#input a count : eg :4
#ans sum of  ( 1+3+5+7...)
#o/p sum = 16
#count=int(input ("enter the number of iterations:"))

#range used :The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
#Syntax:
#range(start, stop, step)
#start:	Optional. An integer number specifying at which position to start. Default is 0
#stop:	Required. An integer number specifying at which position to stop (not included).
#step:	Optional. An integer number specifying the incrementation. Default is 1

#sum() function in Python:
#Python provide an inbuilt function sum() which sums up the numbers in the list.
#Syntax: sum(iterable, start) iterable : iterable can be anything list , tuples or dictionaries , but most importantly it should be numbers.
#start : this start is added to the sum of numbers in the iterable.

#for loop :#for loop concept:A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

count=int(input("Enter count greater than 2:"))
sum=0
for number in range (1,count+1,2):
    print ("The number is " ,number)

    sum=sum+number
    print (sum)
print ("thesumof numbers equal to",sum)
