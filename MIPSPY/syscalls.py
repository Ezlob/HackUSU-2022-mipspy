import sys

from .mips import MIPS

def syscall(mips: MIPS):
    watch = int(mips.registers.get("$v0"))
    match watch:
        case 1: 
            if (mips.registers.get("$a0") != 0):
                try:
                    value = int(mips.registers.get("$a0"))
                except ValueError:
                    
                
            # f12 for double or float
            elif (mips.registers.get("$f12") != 0):
                value = mips.registers.get("$f12")
                print(value)
            return
        case 2 | 3:
            pass
        case 4:
            value = mips.registers.get('$a0')
            print_string(mips.data[mips.data_labels[value]:])
            
        case 5:
            # read_int
            mips.registers["$v0"] = int(input())
            return
        case 6 | 7:
            #read_float or read_double
            mips.registers["$v0"] = float(input())
            return
        case 8:
            # read_string
            str_length = mips.registers.get("$a1")
            input_str = input()
            if(len(input_str) > str_length):
                print("Error! Too many characters in string")
            else:
                # TODO: set this to a memory location specified 
                # by the value of a0, then reset a0 to 0
                mips.registers["$a0"] = input_str
            return
        case 9:
            #sbrk not supported
            return
        case 10:
            # exit
            sys.exit()
        case 11:
            # print_character
            value = mips.registers.get("$a0")
            mips.registers["$a0"] = 0
            print(value)
            return
        case 12:
            # read_character
            input_str = input()
            if(len(input_str) > 1):
                print("Error! Character can only be one byte")
            else:
                mips.registers["$v0"] = input_str
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
            file_to_close = mips.registers.get("$a0")
            mips.registers["$a0"] = 0
            file_to_close.close()
            return
        case 17:
            # exit2
            mips.registers["$a0"] = input()
            sys.exit()

def print_string(bytes: bytearray):
    skip = False
    for pos, byte in enumerate(bytes):
        if skip:
            skip = False
            continue
        
        if byte == 0:
            break
        
        if chr(byte) == '\\':
            # "manage" specials
            next = bytes[pos + 1]
            
            match chr(next):
                case 'n':
                    print('\n', end="")
                case '\\':
                    print('\\', end="")
                case 't':
                    print('\t', end="")
                    
            skip=True
            
        else:
            print(chr(byte), end="")