### string
## string is array of character || combination of character 

a = "Faizan"
print(a)

## some built in function of the string 
## find len use => len() function
# print(len(a))
## use max()
#its work in this way it gives that character which have greatest ASSCI value
# print(max(a))
## use min()
# similarly return the character of lowest ASSCI value
# print(min(a))

### how to concatenate two function
# use + operator concatenation
# first_name = input("Enter your first name:: ")
# last_name = input("Enter your last name:: ")

# full_name = first_name + last_name
# print("You are ",full_name)

## we perform slicing function on the string
## slice[1:3]
print(a[:-2])

### comparing  string
# >, <, <=, >=, !=  => (operators)

name = "Faizan"
print(name==name)
if name != name:
    print("These are not equal")
else:
    print("these name's are equal")



### string formating 
# % percentage or modulus operator its old very method

print("My name is %s and i secured %d in python"%("Faizan", 100));

# use formate() built in function

name = "Faizan Siddique@"
marks = 100
# print("My name is {} and i secured {}".format(name, marks))

print(f"My name is {name} and i secured {marks} marks")  ## can dynamically updated 

### string built in function

  
