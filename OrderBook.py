import json
import os

def findingCP(ticker):
    f = open("./" + ticker + "/noa.json")
    data = json.load(f)
    f.close()
    min = 0.0
    max = 0.0
    for i in data:
        if(i["Direction"] == "ExchangeToNBF"):
            if(max == 0):
                max = i["OrderPrice"]
                print(max)
            if(max < i["OrderPrice"]):
                max = i["OrderPrice"]
                print(max)

for ticker in os.listdir("./"):
    if not ticker.__contains__("."):
       findingCP(ticker)