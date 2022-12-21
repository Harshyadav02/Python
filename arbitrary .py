### Arbitrary argument are for  dyanamic arguments

def avg(* y):
    sum = 0
    for i in y:
        sum = sum +i
    avarage  = sum/len(y)
    return avarage 
value1 = avg(1,2,3,4)
print(value1)
value2 = avg(5,6,7,8,9,10,11,12)
print(value2)
