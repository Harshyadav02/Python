##Tuple are ordered ,indexed , Hetrogenous, Duplicate value,Imuutable

tuple1 = (2,3,4,5,6)
#print(tuple1)
epic = tuple((2,3,1,1,1,'a'))
#print(epic)


for i in epic:
	print("Index ",epic.index(i))
	print("value ",i)
	print("id ",id(i))
	print("type ",type(i))
	print()

## append 
epic.append("HArsh")
print(epic) # will give error

## pop
epic.pop() # will give error


