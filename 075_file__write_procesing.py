with open("files/fegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nCarrot\nCiuciuka")
    myfile.write("\nGarlic")


# now we append a name in the file txt with method a
# a+ method is append and reading and writing method
with open("files/fegetables.txt", "a+") as myappend:
    myappend.write("\nOkra\nJimmy")
    myappend.seek(0)
    content = myappend.read()
    # move te ursor to the zero position

print(content)
