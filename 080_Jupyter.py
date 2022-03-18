# to start jupyter notebook type:     python -m notebook

import os
import time

def path(a):
    while True:
            if os.path.exists(a):
                print("File exist")
                time.sleep(3)
                print("i am happy")
                break
            else:
                print("I can`t find your file :(")
                break

path("files/fruits.txt")

