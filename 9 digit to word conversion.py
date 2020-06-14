#DIGIT WORD CONVERSION PROGRAM
#here i used :int (signed integers) − They are often called just integers or ints, are positive or negative whole numbers with no decimal point.
#and input:When input() function executes program flow will be stopped until the user has given an input.
#if elif and else:you will want to execute a certain line of codes if a condition is satisfied, and a different set of code incase it is not.
#In Python, you have the if, elif and the else statements for this purpose. 

num=int(input("enter a no frm 0 to 12:"))
if num==0:
    print("zero")

elif num==1:
    print("one")
elif num==2:
    print("two")
elif num==3:
    print("three")
elif num==4:
    print("four")
elif num==5:
    print("five")
elif num==6:
    print("six")
elif num==7:
    print("seven")
elif num==8:
    print("eight")
elif num==9:
    print("nine")
elif num==10:
    print("ten")
elif num==11:
    print("eleven")
elif num==12:
    print("twelve")    
else:
    print("enter a num from 1 to 12")
