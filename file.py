file = open('./file.txt', 'a')
file.write("\nThis is a new line!")
file.close()

file = open('./file.txt', 'r')
content = file.read()
file.close()
print(content)