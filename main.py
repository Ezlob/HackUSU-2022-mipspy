#! user/bin/python3

from MIPSPY.mips import MIPS
import sys

# Check if program has file passed to it
if len(sys.argv) != 2:
    print("Make sure to pass in a file dumby")
    sys.exit()


file = sys.argv[1]

# call mips emulator
m = MIPS(file)

m.run()
