#basic progrm for function()
def func():
    print("HI")
print("starting prt")
func()
print("mid prt")
func()
print("end prt")

#Area of circle-calling 
def areaofcircle(r):
    Area=3.14*r*r
    print("area of circle with radius",r,"is ",Area)
areaofcircle(10)
areaofcircle(2)

#printing first x numbers-calling the function with one argument
def fun(x):
    i=0
    while(i<x):
        print(i)
        i+=1
fun(5)
fun(10)

#adding two numbers- calling the function with two arguments
def add2(n,m):
    sum=n+m
    print(sum)
add2(5,2)
add2(m=4,n=1)

#calling the function with arbitrary arguments
def exist(*t):
    for v in t:
        if(v==2 or v==5):
            print("%d exist"%v)
    
exist(1,2,3,4,5,6)

#calling the function with default arguments
def add3(n1,m1=1):
    sum1=n1+m1
    print(sum1)
add3(5,2)
add3(3)


#using global keyword
def add4(n,m):
    global sum
    sum=n+m
    print(sum)
add4(5,2)
print(sum)


