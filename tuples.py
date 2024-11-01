# Tuples in Python
# Tuples are immutable, meaning we can't update or delete individual elements
# Syntax uses comma-separated values in parentheses
# For a single element tuple, use a comma: (2,)

# Creating a tuple
my_tuple = (1, 2, 4, 4, 5)
print("Original tuple:", my_tuple)

# Accessing an element
value = my_tuple[1]
print("Value at index 1:", value)

# Attempting to modify an element (uncommenting the line below will raise an error)
# my_tuple[1] = 10

# Attempting to use pop() (which will raise an error if uncommented)
# my_tuple.pop()

# Reassigning a new tuple and deleting it
my_tuple = (1, 3, 4, 5, 5, 6, 7)
print("New tuple after reassignment:", my_tuple)

# Deleting the entire tuple
del my_tuple
try:
    print(my_tuple)
except NameError:
    print("my_tuple is deleted and no longer accessible")

# Converting a list to a tuple
list1 = [1, 2, 3, 4, 5]
tuple1 = tuple(list1)
print("Converted tuple:", tuple1)

# Converting a tuple to a list
my_list_two = list(tuple1)
print("Converted list:", my_list_two)
