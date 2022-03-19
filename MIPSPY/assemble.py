# open the file
# read each line from the file


# need:
# dictionary for sections/label positions in the code

# an array of each set of instructions in an array taht mirrors it's place in the file as well


# put file into something
# return the something

import sys
import shlex

from typing import Tuple, List, Dict

"""
Assembler
Returns the instructions and labels (in that order) as a tuple

return instruction array, instruction labels, data array, data labels

"""
def assemble(fileName) -> Tuple[List, Dict, List, Dict]:

    file = open(fileName)
    
    instrList = []
    instrLabel = {}
    dataList = []
    dataLabel = {}


    with open(fileName) as file:
        mode = 0 #0 - text / 1 - data
        dataListPos = 0
        instrListPos = 0
        
        for line in file:
            lineAsList = shlex.split(line)
            #This next for loop is just to help find the point where things in a line are just comments, then we'll use that location to boop it out of the list we add to >
            tracker = 0
            for item in lineAsList:
                if item[0] != '#':
                    tracker += 1
                else:
                    break

            lineAsList = lineAsList[:tracker]
            
            if lineAsList: #if not empty
                if lineAsList[0] == ".text":
                    mode = 0
                elif lineAsList[0] == ".data":
                    mode = 1
                else:
                    if mode:
                        #sort data
                        if lineAsList[0][-1] == ':':
                            dataLabel.update({lineAsList[0]: dataListPos})
                            dataList.append(lineAsList[1:])
                            dataListPos += 1
                    else:
                        #sort text
                        if lineAsList[0][-1] == ':':
                            instrLabel.update({lineAsList[0]:instrListPos})
                        else:
                            instrList.append(lineAsList)
                            instrListPos += 1


    return (instrList, instrLabel, dataList, dataLabel)




