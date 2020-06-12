thumb=1
point=2
middle=3
ring=4
small=0
print('Enter the number:')
num = int(input())
result= num%5
print (result)
if result==1:
    print("it is thumb")
if result==2:
    print("it is point")
if result==3:
    print("it is middle")
if result==4:
    print("it is ring")
if result==0:
    print("it is small")
    

