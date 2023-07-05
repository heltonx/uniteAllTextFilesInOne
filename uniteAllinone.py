#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob 

filesArray = glob.glob('*.txt')

fileSum = len(filesArray)

addContent=[]
newLine='\n'

for i in range (fileSum):
	fileVar = open(filesArray[i],'r')
	aux = fileVar.readlines()
	if i > 0: # if is the first loop, not add a new line at the beggining of the file
                addContent.append(newLine) #create new line, to put content below
	addContent = addContent + aux


f = open('uniqueFile.txt','w')
f.writelines(addContent)

