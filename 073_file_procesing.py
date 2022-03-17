my_file = open("files/fruits.txt")

content = my_file.read()

print(content)

# another method to read a file, please use this method
with open('files/fruits.txt') as my_file2:
    content2 = my_file2.read()

print(content2)
