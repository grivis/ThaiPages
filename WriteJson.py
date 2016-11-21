import re
from bs4 import BeautifulSoup
import pickle
import json
import os
import glob

thaidict = {}

f = open('/home/grigory/Python/thai_pages/ThaiDict.dic', 'rb')
thaidict = pickle.load(f)
f.close()

count = 0
for key in thaidict.keys():
    count +=1

print(count, 'keys')


# f = open('/home/grigory/Python/thai_pages/ThaiDict.json', 'w')
# json.dump(thaidict, f)
# f.close()