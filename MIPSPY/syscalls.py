from mips import MIPS

mips = MIPS()

def syscall():
    match mips.registers.get("v0"):
        case 1 | 2 | 3 | 4:
           #print cases
           #a0 for string or int
           if (mips.registers.get("a0") != 0) :
                value = mips.registers.get("a0")
                mips.registers["a0"] = 0
                print(value)
           #f12 for double or float 
           elif (mips.registers.get("f12") != 0):
                value = mips.registers.get("f12")
                mips.registers["f12"] = 0
                print(value)
        case 5:
            #read_int
            mips.registers["v0"] = int(input())
            return
        case 6 | 7:
            #read_float or read_double
            mips.registers["v0"] = float(input())
            return
        case 8:
            #read_string
            str_length = mips.registers.get("a1")
            input_str = input()
            if(len(input_str) > str_length):
                print("Error! Too many characters in string")
                sys.exit()
            else:
                #TODO: set this to a memory location specified by the value of a0
                #rather than putting it in a0
                mips.registers["a0"] = input_str
                return
        case 9:
            #sbrk
            return
        case 10:
            #exit
            return
        case 11:
            #print_character
            return
        case 12:
            #read_character
            return
        case 13:
            #open
            return
        case 14:
            #read
            return
        case 15:
            #write
            return
        case 16:
            #close
            return
        case 17:
            #exit2
            return