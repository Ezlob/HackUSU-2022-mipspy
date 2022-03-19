import sys
from .mips import MIPS

def syscall(mips: MIPS):
    match mips.registers.get("v0"):
        case 1 | 2 | 3 | 4:
            # print cases
            # a0 for string or int
            if (mips.registers.get("a0") != 0):
                value = mips.registers.get("a0")
                mips.registers["a0"] = 0
                print(value)
            # f12 for double or float
            elif (mips.registers.get("f12") != 0):
                value = mips.registers.get("f12")
                mips.registers["f12"] = 0
                print(value)
            return
        case 5:
            # read_int
            mips.registers["v0"] = int(input())
            return
        case 6 | 7:
            #read_float or read_double
            mips.registers["v0"] = float(input())
            return
        case 8:
            # read_string
            str_length = mips.registers.get("a1")
            input_str = input()
            if(len(input_str) > str_length):
                print("Error! Too many characters in string")
            else:
                # TODO: set this to a memory location specified 
                # by the value of a0, then reset a0 to 0
                mips.registers["a0"] = input_str
            return
        case 9:
            #sbrk not supported
            return
        case 10:
            # exit
            sys.exit()
        case 11:
            # print_character
            value = mips.registers.get("a0")
            mips.registers["a0"] = 0
            print(value)
            return
        case 12:
            # read_character
            input_str = input()
            if(len(input_str) > 1):
                print("Error! Character can only be one byte")
            else:
                mips.registers["v0"] = input_str
            return
        case 13:
            # open
            return
        case 14:
            # read
            return
        case 15:
            # write
            return
        case 16:
            # close
            file_to_close = mips.registers.get("a0")
            mips.registers["a0"] = 0
            file_to_close.close()
            return
        case 17:
            # exit2
            mips.registers["a0"] = input()
            sys.exit()
