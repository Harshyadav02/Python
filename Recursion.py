### Function calling itself is called recursive function

### factorail program by Recursion

def fact(x):
    if x == 0 or x ==1:  ### This is base case where our program is to be terminated 
        return 1
    else:
        return x*fact(x-1)
value = int(input("enter the value: "))
result = fact(value)
print("factorail of {} = {} ".format(value,result))

