exit = int(input("Enter the term you wana exit : "))
def fib(prev,curr):
	print(prev)
	print(curr)
	NewTerm = prev+curr
	print(NewTerm)
	for i in range(3,exit):
		prev = curr
		curr = NewTerm
		NewTerm  = prev + curr
		print(NewTerm)

prev = 0
curr = 1
fib(prev,curr)