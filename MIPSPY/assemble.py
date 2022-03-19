# open the file
# read each line from the file


# need:
# dictionary for sections/label positions in the code

# an array of each set of instructions in an array taht mirrors it's place in the file as well


# put file into something
# return the something

import sys

from typing import Tuple, List, Dict

"""
Assembler
Returns the instructions and labels (in that order) as a tuple

return instruction array, instruction labels, data array, data labels

"""
def assembler(fileName) -> Tuple[List, Dict, List, Dict]:

    file = open(fileName)
    
    instrList = []
    instrLabel = {}
    dataList = []
    dataLabel = {}

    
    
    
    #something = instantiated
    instructionsPos = 0
    sectionsPos = 0

    for line in file:
        lineAsList = line.split()


        #This next for loop is just to help find the point where things in a line are just comments, then we'll use that location to boop it out of the list we add to the instructions list later on
        tracker = 0
        for item in lineAsList:
            if item[0] != '#':
                tracker += 1
            else:
                break

        lineAsList = lineAsList[:tracker]
        
        #if we come across .data, then we need to boop then next lines into the data array and data dict until we come across another .label with 

    for item in instructions:
        print(f"{item}")

    print(f"{sections}")

if __name__ == '__main__':
    assembler(sys.argv[1])



