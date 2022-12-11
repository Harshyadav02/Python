'''# Creation of list
# It is ordered , indexed , hetrogenous value ,duplicate value,mutable  
list1 = ["harsh","Mca1st" , "xyz@gmail.com"]
print(list1[0])
print(list1)

# Adding an element at last 

# without aditional variable :-
list1.append ("545435")
print(list1)

# without additional Element :-

phone ="4545511"
list1.append(phone)
print(list1)

# At Specific Index:-

list1.insert(0,2332)
print(list1)


# LIFO 

list1.pop()
print(list1)

# By Remove Method
list1.remove(list1[0])
print(list1)'''

'''for i in range (0,3):

	name = input("ENter the name of Student ")
	cnt = input("ENter the cnt of Student ")
	class1 = input("ENter the class of Student ")
	mail = input("ENter the mail of Student ")
	if i == 0:
		stud1 = [" my name is {} my contact is {}  my class is {} and my mail is {}".format(name,cnt,class1,mail)]
	if i == 1:
		stud2 = [" my name is {} my contact is {}  my class is {} and my mail is {}".format(name,cnt,class1,mail)]
	if i ==2:
		stud3 = [" my name is {} my contact is {}  my class is {} and my mail is {}".format(name,cnt,class1,mail)]

print(stud1)
print(stud2)
print(stud3)'''

list1 = [1,2,3,4,5]
list1.append(34)
print(list1)
print(id(list1))
list1.remove(2)
print(list1)

print(id(list1))
list2 =[5,6,7,"harsh"]
list1 =list1 + list2
print(list1)

for i in list2:
	list1.append(list2)
print(list1)