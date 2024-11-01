
### arrray 
# in the python we use square bracket to decalare the array

array = [1,2, 3, 4, 5, 6, 7]
num = array[0]   ## can access value by this method 
array[0] = 5     ## can update

# print(num)

# use for loop to print the array
for element in array:
    print(element)

## use for loop to print the array
i = 0
while(i < len(array)):
    print(array[i])
    i +=1

### Array build function
array.append(1)
array.pop()
array.insert(2, 4)
result = array.count(1)
array.sort()
array.reverse()
print(max(array))
print(min(array))
print(3 in [array])  ## check member ship
