def mixString(s1, s2):
  resultString = s1[:1] + s2[:1] + s1[int(len(s1) /2):int(len(s1) /2)+1] +s2[int(len(s2) /2):int(len(s2) /2)+1] +s1[len(s1)-1] + s2[len(s2)-1]
  print("Mix String is ", resultString)
  
s1 = "Avyukta"
print(s1[:1])
print(len(s1))
print(len(s1)/2)
print(len(s1)/2+1)
print(len(s1)/2-1)
s2 = "Jayaprakash"
print(s2[:1])
print(len(s2))
print(len(s2)/2)
print(len(s2)/2+1)
print(len(s2)/2-1)
mixString(s1, s2)
