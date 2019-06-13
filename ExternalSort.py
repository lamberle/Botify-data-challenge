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

class heapnode:
    """elem : first elem of file, file : sorted file to merge"""

    def __init__(self, elem, file,):
        self.elem = elem
        self.file = file
    def nextElem(self):
        self.elem = self.file.readline().strip()
    def closeFile(self):
        self.file.close()

class ExternalMergeSort :
    """Attributes:
        subFilesPath : list of the sorted subfiles
        heapnodes : list of heapnodes"""
    def __init__(self):
        self.subFilesPath = []
        self.heapnodes = []
        
    #Generate sorted subfiles of specified number of lines for the input file
    def splitFile(self,fileName, subFilesSize):
        file = open(fileName,"r+")
        size = 0
        subfileIndex = 0
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
                    filePath = TEMP_FILES_PATH + "subfile"+str(subfileIndex)+".txt"
                    self.subFilesPath.append(filePath)
                    f= open(filePath,"w+")
                    f.writelines(subfileContent)
                    f.close();
                    subfileIndex +=1
                    subfileContent = []
    def printFilesPaths(self):
        for filePath in self.subFilesPath:
            print(filePath)
    def createHeapNodes(self):
        for filePath in self.subFilesPath:
            f = open(filePath,"r+")
            self.heapnodes.append(heapnode(f.readline().strip(),f))
    def sortMerge(self,ouputFileName):
        file = open(ouputFileName,"w+")
        self.createHeapNodes()
        for node in self.heapnodes:
            print(node.elem)
        while True :
            min = self.getMinHeap()
            if not min:
                break      
            file.write(min +"\n")
        for node in self.heapnodes:
            node.closeFile()
        file.close()
        
    def getMinHeap(self):
        min = self.heapnodes[0].elem
        minIndex = 0
        index = 0
        for node in self.heapnodes:
            if node.elem and node.elem <= min:
                min = node.elem
                minIndex = index
            index += 1
        self.heapnodes[minIndex].nextElem()
        return min
            
        

merge = ExternalMergeSort()               
merge.splitFile(INPUT_FILE_NAME,BLOCK_SIZE)
merge.printFilesPaths()
merge.sortMerge(OUTPUT_FILE_NAME)

f= open("Temp/subfile0.txt","r+")
while True:
    line = f.readline()
    print("LINE : " + line)
    if not line:
        break
f.close()

            
            
        
            