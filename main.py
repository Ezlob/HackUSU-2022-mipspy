#! user/bin/python3

import argparse
from MIPSPY.mips import MIPS
import sys
import wrapper

#run mode, debug mode

parser = argparse.ArgumentParser()
parser.add_argument('-d', help = 'run the file in debug mode')
args = parser.parse_args()


# Check if program has file passed to it
if len(sys.argv) < 2:
    print("Make sure to pass in a file dumby")
    sys.exit()


file = sys.argv[1]

# call mips emulator
m = MIPS(file)


# THIS IS WHERE WE WILL TIE IN THE GUI
m.run()
