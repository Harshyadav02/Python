## functions

### def key word is used to create a function 

##### syntax :- def < functionName >(parmeters or argumnts):
				## body

### area of rantagle by function

def rect_area():
	length = int(input("enter the length"))
	width = int(input("enter the breadth"))
	area = length * width
	print(area)
rect_area()

### factorail by function 

def factorial(m):
	fact =1
	if(m == 1):
		return 1
	else :
		for i in range(1,m+1):
			fact = fact*i
	return fact
for i in range(3):
	choice = int(input("enter the choice "))
	fact_value = factorial(choice)
	print("factorail of ",choice ,"is = ",fact_value)
