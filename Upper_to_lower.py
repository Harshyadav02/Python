### upper to lower without lower,upper method

value = input(" Enter the value ")

empty = ""

for i in value:
	if ord(i) >= 65 and ord(i)<= 90:
		a = ord(i)+32
		b = chr(a)
		empty = empty+b
	# elif ord(i) >= 97 and ord(i)<= 122:
	# 	empty = empty+i
	else:
		 empty = empty + i 
print("value before conversion ",value)
print("value after conversion ",empty)
