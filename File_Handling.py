### File Handling 

## file(text file/.txt)

### Basic operation  on file :- CRUD --- create,read,update,delete

#### update is done in two way -- APPEND , OVERWRITE

''' var = open("intro.txt","a") ### Append Operation  
var.write("HARSH")
var.close()

var = open("intro.txt","r") ### Reading Operation 
data = var.read()
print(data)
var.close() '''

''' f = open("telephone.txt ","a") ## " a " creates a file if not present 
name = input("Enter your name:  ")
age = input("Enter your age: ") 
city = input("Enter your city: ")
details = "Hi I am {}.\nI am {} year old.\nI live in {}. ".format(name,age,city)
print(details)
f.write(details) ## data will be witten in Telephone .txt file 
f.close() '''

f = open("telephone.txt","r")
data =f.read() 
print(data)
f.close()