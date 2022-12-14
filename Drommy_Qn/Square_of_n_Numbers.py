list1 = []
for x in range (0,6):
	i  = int(input())
	list1.append(i)

sum1 = 0;
for i in list1:
	sum1 = sum1+list1[i-1]*list1[i-1]

print("sum  = ",sum1)



