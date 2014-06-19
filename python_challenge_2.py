# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 23:13:40 2014

@author: adrianma
"""

import urllib
from collections import Counter

# Read the HTML source and store it
oSock = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
tHtmlSource = oSock.read(); 
oSock.close();

# Find the most common character within the HTML source and print it out
vCharacterFreq = Counter(tHtmlSource.strip())
print(vCharacterFreq.most_common()[-1])

# Solution is the work 'equality'. Reasoning missing, found solution online