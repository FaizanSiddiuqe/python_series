### list is similar to array but a little difference between that we can store differenct type of data

## SYNTAX

list = [1, 3, 'a', "Faizan Siddique"]
result =list[3]
print(result)
## display using for loop

for element in list:
    print(element)

### built in funciton of list

## find the length of the list
print(len(list))
## append()
list.append(2)
## insert()
list.insert(2, "Hi Faizan")
## count()
result1 = list.count(3)
## pop()
list.pop()
## index()
list.index(1)
## membeship
# result3 = 3 in list
## clear()
# list.clear()   ## will clear all the element
## remove
list.remove(3)
print(list)



