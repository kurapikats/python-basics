# sqaure of numbers range from 0 to 9, but show only squres that are even
list = [x**2 for x in range(10) if x**2 % 2 == 0]
print(list)
