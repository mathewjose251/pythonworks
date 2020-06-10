#FIND ALL OCCURRENCES OF "NAME" IGNORING THE CASE  
#STRINGS: Strings are amongst the most popular types in Python. We can create them simply by enclosing characters in quotes.
#Python treats single quotes the same as double quotes. Creating strings is as simple as assigning a value to a variable. 

inputString = "my name is AVYU,avyu is my name"
substring = "AVYU"
tempString = inputString.lower()
count = tempString.count(substring.lower())
print("The AVYU count is:", count) 
