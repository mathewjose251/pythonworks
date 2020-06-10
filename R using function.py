#if
def func1():
    x=2
    y=3
    global result
    result=x*y
    if(result==6):
        print(result)
func1()
#for
def func2():
    global i
    x=[1,2,3,4,5,6,0]
    i=0
    for j in x:
      if(j%2==0):
         i+=1
      print("The number of even numbers are",i)
func2()
#while
def func3():
    global r
x=5
a=0
while(a<=5):
    print(a)
    a+=1
func3()
#multiply
ans=result*i*r

print(ans)
