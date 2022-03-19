#! user/bin/python3

import argparse
from MIPSPY.mips import MIPS
import sys
from MIPSPY.mips_wrapper import debugger

#run mode, debug mode

parser = argparse.ArgumentParser(description="Run MIPS files normally or use debug mode to traverse the file line by line")
parser.add_argument("-d", "--debug",  help = 'run the file in debug mode', action = "store_true")
parser.add_argument("file", type=str, help="the mips file")
args = parser.parse_args()


# Check if program has file passed to it
if len(sys.argv) < 2:
    print("Make sure to pass in a file dumby")
    sys.exit()

#put into MIPS
if len(sys.argv) > 2:
    if sys.argv[2] == '-d':
        m = debugger(args.file) #if we run in debug mode

else:
    m = MIPS(args.file) #default

# this is what runs the program
m.run()
