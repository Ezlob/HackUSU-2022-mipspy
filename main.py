#! user/bin/python3

import argparse
from pickle import TRUE
from MIPSPY.mips import MIPS
import sys
from MIPSPY.mips_wrapper import debugger

# run mode, debug mode

parser = argparse.ArgumentParser(
    description="Run MIPS files normally or use debug mode to traverse the file line by line"
)
parser.add_argument(
    "-d", "--debug", help="run the file in debug mode", action="store_true"
)
parser.add_argument("file", type=str, help="the mips file")
args = parser.parse_args()

m: MIPS
DEBUG = False

# put into MIPS
if "-d" in sys.argv:
    sys.argv.remove("-d")
    DEBUG = TRUE  # if we run in debug mode

# Check if program has file passed to it
if len(sys.argv) < 2:
    print("Make sure to pass in a file dumby")
    sys.exit()

# Check if program has file passed to it
if len(sys.argv) < 2:
    print("Make sure to pass in a file dumby")
    sys.exit()

# put into MIPS
if DEBUG:
    m = debugger(args.file)  # if we run in debug mode
    m.debug_loop()
else:
    m = MIPS(args.file)  # default
    m.run()
