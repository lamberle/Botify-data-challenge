# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:10:53 2019

@author: Léo
"""

UNSORTED_FILE_NAME = "unsorted.txt"
SORTED_FILE_NAME = "sorted.txt"



def sortCheck(unsorted_file_name,sorted_file_name):
    
    unsortedFile = open(unsorted_file_name,"r+")
    sortedFile = open(sorted_file_name,"r+")
    
    unsortedLines = unsortedFile.readlines()    
    sortedLines = sortedFile.readlines()
    
    unsortedFile.close()
    sortedFile.close()
    
    correction = sorted(unsortedLines)
    
    if len(sortedLines) != len(correction):
        return 0
    
    for i in range(len(correction)):
        if(sortedLines[i].strip() != correction[i].strip()):
            return 0
    return 1

if(sortCheck(UNSORTED_FILE_NAME,SORTED_FILE_NAME) == 0):
    print("Le résultat du tri ne correspond pas au résultat attendu")
else:
    print("Le test est passé avec succès !")
        