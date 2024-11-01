## conditional statement
### in the 
num = 1  ## take a integer number

## condition statement
# if(num == 1):
#     print("Condition is statisfied")
# else:
#     print("Condition is not statisfied")

### how to multilple or nested if else statement
 
if(num > 0):
    if(num == 1):
        print("Condition is statisfied")
    else:
        print("Conditon is not statisfied")
else:
    print("Please enter Positive number")
    
### use if else and elif

#take the age from the user and print the that's is he able to vote or not

age = int(input("Enter your age:: "))

if(age > 0):
    if(age < 18):
        print("You are not able to vote")
    elif(age == 18 or age > 18):
        print("You are able to vote")
else:
    print("Please enter the povitive number")
    
## print even and odd number using if else conditon
num = int(input("Enter number::"))

if(num > 0 and num % 2 == 0):
    print("You entered the even number")
else:
    print("you entered the odd number")
        