# python pip3 install pandas
# python -m pip install mitmproxy
# pandas is a several of modules

# in cmd: python3/import sys/sys.prefix
import pandas
import time
import os

while True:
    if os.path('files/temperatures.csv'):
        data  = pandas.read_csv("files/temperatures.csv")
        print(data.mean())
        time.sleep(5)
    else:
        print("I can`t find your file.")
        break
 