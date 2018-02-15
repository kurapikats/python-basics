# sets: accepts only unique values and it's immutable

numbers = {1, 2, 3, 4, 5, 6}
print(5 in numbers)

numbers.add(9)
print(numbers)

numbers.remove(4)
print(numbers)

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# union operation - no duplicate entries
# 1,2,3,4,5,6,7,8
print(setA | setB)

# intersection operation
# returns 4, 5
print(setA & setB)

# difference
print(setA - setB)
