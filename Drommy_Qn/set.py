# hold unique value ,unordred,hetergenous,mutable

######  Creation of set    #####

star = {3,2,4,6,7,8,2,"A","B"}
#star = set((2,3,4,5,6,2))
print(star)

##### READING ####

for i in star:
	print(i,end = " ")

#### pop ####

'''
star.pop() ## random hatega bhai never use it
print(star)

'''

#### Remove  ####

star.remove(3)
print(star)


#### discard ####

star.discard("A")
print(star)  ### dicard doesn't provide any error if the elemnt is does not exist in set