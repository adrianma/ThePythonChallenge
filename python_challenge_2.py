# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 23:13:40 2014

@author: adrianma
"""

my_dict = {
    ' ':' ','.':'.','(':'(',')':')','a':'c','b':'d','c':'e','d':'f', \
    'e':'g','f':'h', 'g':'i','h':'j','i':'k','j':'l','k':'m','l':'n','m':'o', \
    'n':'p','o':'q','p':'r','q':'s','r':'t','s':'u','t':'v','u':'w','v': \
    'x','w':'y','x':'z','y':'a','z':'b'
}

tPart1 = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'
tPart2 = 'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

tEnglish1 = ''.join([my_dict[sIdx] for sIdx in tPart1])
tEnglish2 = ''.join([my_dict[sIdx] for sIdx in tPart2])
    
print tEnglish1 + tEnglish2

# What should be changed in the URL
print ''.join(my_dict[sIdx] for sIdx in 'map')


