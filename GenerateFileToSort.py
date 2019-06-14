# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 17:39:26 2019
Program that generate a file txt with NB_WORD lines composed of 1 to WORD_MAX_LENGTH random characters
@author: Léo
"""

import string
import random


POSSIBLE_CHAR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
WORD_MAX_LENGTH = 20
NB_WORD = 500
FILE_NAME = "unsorted.txt"

f= open(FILE_NAME,"w+")
for i in range(NB_WORD):
    word_length = int(random.random()*WORD_MAX_LENGTH)+1
    for j in range(word_length):
         f.write(random.choice(POSSIBLE_CHAR))
    f.write("\n")
     
f.close() 