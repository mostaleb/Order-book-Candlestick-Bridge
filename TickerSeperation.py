import json
import os
import datetime as dt
from datetime import datetime
import time

def dumpJSON(filename, tickername, list, state):
    json_data = json.dumps(list)
    with open(tickername + "/" + filename, state) as outfile:
        outfile.write(json_data)

def loadFile(tickerName):
    return open(tickerName + "/noa.json")

f = open("TSXData.json")
data = json.load(f)
f.close()

i = {}
trade = []
cancelled = []
noa = []
tickerList = []
list = []

for i in data:

    if i["Symbol"] == "P29R0":
        list.append(i)
        if(i["MessageType"] == "Trade"):
            trade.append(i)
        if(i["MessageType"] == "Cancelled"):
            cancelled.append(i)
        if(i['MessageType'] == "NewOrderAcknowledged"):
            noa.append(i)
 
if not os.path.isdir("./P29R0"):
        
    os.makedirs("./P29R0")

dumpJSON("trade.json", "P29R0", trade, "w")
dumpJSON("noa.json", "P29R0", noa, "w")  
dumpJSON("cancelled.json", "P29R0", cancelled, "w")

file1 = loadFile("P29R0")
loadedNoa = json.load(file1)
file1.close()

file2 = loadFile("P29R0")
loadedCancelled = json.load(file2)
file2.close()

counterb = 0
countera = 0
for i in loadedNoa:
    if i["Direction"] == "ExchangeToNBF":
        counterb += 1
    for j in loadedCancelled:
        if(i["OrderID"] == j["OrderID"] and j["Direction"] == "ExchangeToNBF"):
            counterb -= 1

for i in loadedNoa:
    if i["Direction"] == "NBFToExchange":
        countera += 1
    for j in loadedCancelled:
        if(i["OrderID"] == j["OrderID"] and j["Direction"] == "NBFToEXchange"):
            countera -= 1
