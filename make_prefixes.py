# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 20:55:13 2015

@author: killerdigby
"""

from urllib import urlopen
from xml.dom import minidom
import json

#Canadian area codes
area_codes = [403, 587, 780, 236, 250, 604, 778, 204, 431, 
              506, 709, 867, 782, 902, 867, 226, 249, 289, 
              343, 365, 416, 437, 519, 613, 647, 705, 807, 
              905, 782, 902, 418, 438, 450, 514, 579, 581, 
              819, 873,306, 639, 867, 600, 622, 800, 844, 
              855, 866, 877, 888]
              
#add lists of local prefixes to dict 
area_prefixes ={}
for area_code in area_codes:
    area_prefixes[area_code] = []
    url = "http://www.localcallingguide.com/xmlprefix.php?npa="+ str(area_code)
    xml_str = urlopen(url).read()
    xmldoc = minidom.parseString(xml_str)
    area_code_prefixes = xmldoc.getElementsByTagName('nxx')
    for i in area_code_prefixes:
       area_prefixes[area_code].append(i.firstChild.nodeValue)
    if not area_prefixes[area_code]:
        area_prefixes.pop(area_code)

#dump area code prefix dict to file using json       
with open('area_prefixes.json', 'w') as f:
    json.dump(area_prefixes, f)       