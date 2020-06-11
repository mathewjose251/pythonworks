#There are four collection data types in the Python programming language:
#List: is a collection which is ordered and changeable. Allows duplicate members.
#Tuple: is a collection which is ordered and unchangeable. Allows duplicate members.
#Set: is a collection which is unordered and unindexed. No duplicate members.
#Dictionary: is a collection which is unordered, changeable and indexed. No duplicate members.
print("list")
#list: A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

#1
#as you can see in list we use [] square brackets 

alist = ["avyu ", "arjun", "juan"]
print(alist)
print("$$$$$$$$$$$$$$$$$$$$$$$")
#2
#You access the list items by referring to the index number:

blist = ["arjun ", "is", "stupid"]
print(blist[2])
print("$$$$$$$$$$$$$$$$$$$$$$$")


print("tuple")
#tuple:A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#1
#as you can see in tuple we use () round brackets

atuple = ("car", "bike", "scooter")
print(atuple)
print("$$$$$$$$$$$$$$$$$$$$$$$")

#2
#You can access tuple items by referring to the index number, inside square brackets
btuple = ("i", "luv", "python")
print(btuple[2])
print("$$$$$$$$$$$$$$$$$$$$$$$")


print("sets")
#sets:A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
#1
#as you can see in set we use {} curly brackets
aset= {" we r "," doing "," covidpython "}
print(aset)
print("$$$$$$$$$$$$$$$$$$$$$$$")

#2
#Loop through the set, and print the values:
bset = {"apple", "banana", "cherry"}

for x in bset:
  print(x)
print("$$$$$$$$$$$$$$$$$$$$$$$")


print("dictionary")
#dictionary:A  dictionary is a collection which is unordered, changeable and indexed.
#In Python dictionaries are written with curly brackets, and they have keys and values.
#1
adict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(adict)

#2
#Change the "birth" to 2004:

bdict = {
  "name": "avyu",
  "organism": "human",
  "birth": 2020
}
bdict["birth"] = 2004

print("$$$$$$$$$$$$$$$$$$$$$$$")


print("***************************************************************************************************************************************************")


#part2

#list
#Negative Indexing:
#Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
clist = ["apple", "banana", "cherry"]
print(clist[-3])
print("$$$$$$$$$$$$$$$$$$$$$$$")

#tuple
#Negative Indexing
#Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
#Print the last item of the tuple:

ctuple = ("apple", "banana", "cherry")
print(ctuple[-2])
print("$$$$$$$$$$$$$$$$$$$$$$$")

#set
#Check if "banana" is present in the set:

cset = {"apple", "banana", "cherry"}
print("banana" in cset)
print("$$$$$$$$$$$$$$$$$$$$$$$")

#dictionary
#Loop Through a Dictionary
#You can loop through a dictionary by using a for loop.
#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
cdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in cdict.items():
  print(x, y)
  print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")




