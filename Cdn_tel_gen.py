# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 22:33:19 2015

@author: killerdigby
"""

from random import randint
from random import choice 
import json

class CdnPhoneGen:
    
    def __init__(self):
        with open('area_prefixes.json', 'r') as f:
            self.area_prefixes = json.load(f)
            
    def get_number_in(self, area_code):
        head = choice(self.area_prefixes[str(area_code)])
        tail = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
        return "{0}-{1}-{2}".format(area_code, head, tail)
     
    def get_random(self):
        area_code = choice(self.area_prefixes.keys())
        head = choice(self.area_prefixes[area_code])
        tail = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
        return "{0}-{1}-{2}".format(area_code, head, tail)
      
gen = CdnPhoneGen()

print gen.get_random()
print gen.get_number_in(902)     