value = input("Enter the value ")

if value == value[::-1]:
	print("Given Value is Plandriom")
else:
	print("Not an Plandriom")

for i in range (len(value)):
	i[0] = i[len(i)-1]
	