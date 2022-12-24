## functions
#### def key word is used to create a function 

##### syntax :- def < functionName >(parmeters or argumnts):
				## body

### area of rectangle by function

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

def squareroot(m):
	error = float((input("Enter the desired error: ")))
	g2=m/2
	g1=m/g2
    
    
	while abs(g1-g2) >error:
		
		g1=g2
		g2=float((g1+(m/g2)))/2	
	return g2
value = int(input("enter the desired value: "))
print(squareroot(value))