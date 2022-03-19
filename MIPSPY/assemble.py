
#open the file
#read each line from the file


#need:
#dictionary for sections/label positions in the code

#an array of each set of instructions in an array taht mirrors it's place in the file as well


#put file into something
#return the something

import sys

from typing import Tuple

"""
Assembler
Returns the instructions and labels (in that order) as a tuple

"""
def assembler(fileName) -> Tuple[List, Dict]:

    file = open(fileName)
    
    sections = {}
    instructions = []

    
    
    #something = instantiated
    instructionsPos = 0

    for line in file:
        lineAsList = line.split()

        instructions[instructionsPos] = lineAsList
        
        for item in lineAsList:
            if item[0] == '.' or item[-1] == ':':
                sections.update({item: instructionsPos}) #update dict with section or label
        
        instructionsPos += 1

    print(f"{instructions}")




