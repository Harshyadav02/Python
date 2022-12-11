#UpperCase in String

'''str1= "Harsh"
print(str1)
str2 = str1.upper()
print(str2)

# Lower Cse in Strings
str3 = str1.lower()
print(str3)
for i in str1:
	print(i)'''

# length of string

'''name = input(" Enter the name ")

count = 0;
for i in name:
	count+=1
print(count)'''


# program fOR camel case 
'''value1 = input("Enter the name ")
value2 = ''
for i in range(len(value1)):
	if i == 1:
		value2 = value2 + value1[i].upper()
	
	else:
		value2 = value2 + value1[i].lower()
print(value2)


value1 = value1.upper()
print(value1)'''


# Note :- typing ke doran hone vali galtiya  is called Typo	
s1 = "noon".strip()
s2 = "noon ".strip()

if s1 == s2:
	print("s1 is equal to s2 ")
else :
	print("Not equal")

# Reverse an string :-

'''str1  = input("ENter the string ")

str2 = " "

for i in range(len(str1)-1 ,-1,-1):
	str2 = str2 + str1[i]
print("user input is {}".format(str1))
print("reversed string is {}".format(str2))'''

str1  = input("ENter the string ")

str2 = str1[::-1]

print("user srting = ",str1)
print("str2 = ",str2)
