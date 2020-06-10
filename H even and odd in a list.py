#count and print even numbers and odd numbers in a

#a list is used

#variable: i and x, example:x=[1,2,3,4,5,,0] and i=0

#for loop concept:A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

#arthematic operator : modulus (%):The modulus operator, sometimes also called the remainder operator or
# integer remainder operator works on integers (and integer expressions) and
# yields the remainder when the first operand is divided by the second.
# In Python, the modulus operator is a percent sign ( % ).

#concept used is odd and even

#comparison opertors used : == means equal and != means not equal example
# in the 1st program :if(j%2==0)
#in the 2nd part :if(j%2==0)

x=[1,2,3,4,5,6,0]
i=0
for j in x
   if(j%2==0):
     print(j)
     i+=1
print("The number of even numbers are",i)
i=0
for j in x:
   if(j%2!=0):
     print(j)
     i+=1
print("The number of odd numbers are",i)

