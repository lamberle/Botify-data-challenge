# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:00:10 2019

@author: Léo
"""


INPUT_FILE_NAME = "unsorted.txt"
OUTPUT_FILE_NAME = "sorted.txt"
BLOCK_SIZE = 100
TEMP_FILES_PATH = "Temp/"

start_index = 0
end_index = start_index + BLOCK_SIZE

#Generate sorted subfiles of specified number of lines for the input file
def splitFile(fileName, subFilesSize):
    file = open(fileName,"r+")
    size = 0
    subfileIndex = 1
    subfileContent = []
    while True:
        line = file.readline()
        if not line:
            break
        subfileContent.append(line)
        size += 1
        if size == BLOCK_SIZE:
                size = 0
                subfileContent = sorted(subfileContent)
                f= open(TEMP_FILES_PATH + "subfile"+str(subfileIndex)+".txt","w+")
                f.writelines(subfileContent)
                f.close();
                subfileIndex +=1
                subfileContent = []

                
splitFile(INPUT_FILE_NAME,BLOCK_SIZE)


            
            
        
            