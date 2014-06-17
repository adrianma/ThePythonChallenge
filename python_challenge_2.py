# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 23:13:40 2014

@author: adrianma
"""

import urllib

sock = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
htmlSource = sock.read(); 
sock.close();
print htmlSource

