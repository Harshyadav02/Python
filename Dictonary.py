# Dictionary are mutable , ordered, indexed,and hetrognous and hold data in form of key and value
 
### use dictionary in unstrured data


### Creation #####

dict1 = {"name" : "harsh", "class" : "MCA", "subject" : "python"}  
print(dict1)

for i in dict1:
	print(i) #will print keys
	print(dict1[i]) # will print values

for i,j in dict1.items(): ## will print both keys as well as value
	print(i)
	print(j)

dict2 = {1:23,2:5,3:'7',3:'8'} ## keys cant be duplicate but value can be coz index is done by keys
for i,j in dict2.items():
	print(i)
	print(j)


### update ###

dict1["name"]= "yadav"

print(dict)
### adding new key  ###

dict1["school"] = "ni pta"
print(dict1)

### pop() ### always give key 
dict1.pop("school") ## Note:- pop have an argument usally we don't give an argument
print(dict1)