
#open the file
#read each line from the file


#need:
#dictionary for sections/label positions in the code

#an array of each set of instructions in an array taht mirrors it's place in the file as well


#put file into something
#return the something


def assembler(fileName):

    file = open(fileName)
    
    sections = {}
    instructions = []

    
    
    #something = instantiated
   instructionsPos = 0

    for line in file:
        instructions.append(line)
        tempObj = line.split()
        for item in tempObj:
            if item[0] == '.' or item[-1] == ':':
                sections.update({item: instructionsPos})
        

