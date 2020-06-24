#TO FIND N NO:S WITH AVERAGE 
#FOR LOOP
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
#FUNCTIONS
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.
#RETURN
#The return keyword is to exit a function and return a value.


def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

print("The average is", cal_average([1,2,3]))
