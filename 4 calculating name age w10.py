#using functions:A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.
#in my program: the 2 arguments are name and age nd birthyear is also calculated
#in this program arthematic operator is used an it is - (subtraction)
def calculation_of_age(name,age):
    birthyear=2020-age
    print("Hello," + name, "you born in the year: " + str(birthyear))
    print("*******************************")

calculation_of_age('avyu',16)
calculation_of_age('arjun',24)
calculation_of_age('juan',6)

