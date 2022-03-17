import os
import time

while True:
    if os.path.exists('files/fruits.txt'):
        with open("files/fruits.txt") as file:
            print(file.read())
            time.sleep(5)
            break
    else:
        print("Sory, but i don`t find your file :( ")
        time.sleep(5)
        break
