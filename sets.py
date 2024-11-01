### sets like tuple are also immute able and can't access their value with index
## can't access their value due to its unodered
## can store differnet data type values like string, int , float etc
## can update with add()  and  update() function
## can delte the value with remove() and discard() function
# use curly braces to declare the set 
# can perfrom various operatrion like union , intersection and also difference
## can also declare using built in function set()
### can display using loops
### SYNTAX

my_set = {1, 3, 4,"Faizan Siddique", "Json smith"}

# print the set
# print(my_set)

## try to access the value with index

# set_value = my_set[1]  ## show error because of unodered element
# print(set_value)

## declare using built in function
# in this case we will pass list
my_set1 = set([1, 3, 4, 5, 6, "Faizan Siddiue"])
print(my_set1)

# empty set
empty_set = set()
print(empty_set)
# another empty set
another_empty_set = {}
print(another_empty_set)

## add()
# we use to add the one element in the set
my_set1.add(12)
print(my_set1)
## update method 
# use to add multiple and different data type data
my_set1.update([11, 13, 14, "Faizan"])
print(my_set1)

### important thing is that when we use update function if we similar data if they exist already in the set no change will be done

## remove()
# use to remove the value
# my_set1.remove(0)
# print(my_set1)
## discard function
# my_set1.discard(0)
# print(my_set1)

### the difference between remove and discard is that if element is not present in the set which is passed in the function it will show err but discard does not show any error if passed element is not present in the set

# for element in my_set1:
#     print(element)
