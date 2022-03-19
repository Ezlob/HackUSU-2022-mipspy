#! user/bin/python3

import argparse
from MIPSPY.mips import MIPS
import sys
from MIPSPY.mips_wrapper import debugger

#run mode, debug mode

parser = argparse.ArgumentParser(description="Run MIPS files normally or use debug mode to traverse the file line by line")
parser.add_argument("-d", "--debug",  help = 'run the file in debug mode', action = "store_true")
args = parser.parse_args()


# Check if program has file passed to it
if len(sys.argv) < 3:
    print("Make sure to pass in a file dumby")
    sys.exit()


file = sys.argv[1]

# call mips emulator

if sys.argv[2] == '-d':
    m = debugger(file)

else:
    m = MIPS(file)


# this is what runs the program
m.run()
