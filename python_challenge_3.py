# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 20:40:54 2014

@author: adrianma
"""

import urllib
import re

# Read the HTML source and store it
oSock = urllib.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
tHtmlSource = oSock.read(); 
oSock.close();

# Takes advante of the findall() function from re
# Solution taken from : 
# http://www.iainbenson.com/programming/Python/Challenge/solution3.php
result = "".join(re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]',tHtmlSource))

print result