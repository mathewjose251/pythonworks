
#maam's work purpose of sending work: to study 
# STATEMENTS 
#print statements
c=100
d=50
print("Different ways to print")
print('Different ways to print')
print(c)
print("The value of c is",c)
print("%d is the value of c"%c)
print("%f is the value of c"%c)
print("{} and {} are the numbers".format(c,d))
print("{} and {} are the numbers".format(d,c))


#conditional statement
#if statement
#check whether the entered number is zero

a=int(input("Enter a number\n"))
if a==0:
    print("Number is zero")
print("Out of the program")



#if else statement
#check whether the entered number is divisible by 3 or not

x=int(input("Enter a number"))
if x%3==0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")
print("Out of the program")



#if elif else statement
#check whether the entered number is positive or negative


y=int(input("Enter a number"))
if(y==0):
    print("Number is zero")
elif(y>0):
    print("Number is positive")
elif(y<0):
    print("Number is negative")
