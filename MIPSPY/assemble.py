# open the file
# read each line from the file


# need:
# dictionary for sections/label positions in the code

# an array of each set of instructions in an array taht mirrors it's place in the file as well


# put file into something
# return the something


from typing import Tuple, List, Dict

"""
Assembler
Returns the instructions and labels (in that order) as a tuple

return instruction array, instruction labels, data array, data labels

"""


def assembler(fileName) -> Tuple[List, Dict, List, Dict]:

    file = open(fileName)

    sections = {}
    instructions = []

    # something = instantiated
    instructionsPos = 0

    for line in file:
        instructions.append(line)
        tempObj = line.split()
        for item in tempObj:
            if item[0] == "." or item[-1] == ":":
                sections.update({item: instructionsPos})
