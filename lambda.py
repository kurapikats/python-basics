# normal function
def square(x):
    return x**2


print(square(4))

# same as above done in lambda expression
# this is also called anonymous function
result = (lambda x: x**2)(4)
print(result)
