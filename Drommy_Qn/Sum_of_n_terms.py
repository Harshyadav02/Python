n = int(input("enter the range"))
Nterm  = int(input("enter the term you wanna add ")) 

list1  = []
for i in range(0,n):
	i = int(input("Enter the value "))
	list1.append(i)

firsTerm= list1[0]
diff = list1[1]- list1[0]

for i in range(0,Nterm+1):
	 
	sum1 = (Nterm/2)*(2*firsTerm+(Nterm-1)*diff) ## Arithmatic Progression Forumla
print(sum1)

