value  = int(input(" Enter the number "))

fact = 1
for i in range(1,value+1):
	if i == 0 and i ==1:
		print("{} is 1  of {}".format(fact,i))
	else:
		fact = fact*i
		i= i+1
print(" Fact of {} is {} ".format(value,i))