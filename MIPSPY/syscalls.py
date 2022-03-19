def syscall(v):
    match v:
        case 1 | 2 | 3 | 4:
           #print cases
           #a0 for string or int
           if (Dict.get("a0") != 0) :
                value = Dict.get("a0")
                Dict["a0"] = 0
                print(value)
           #f12 for double or float 
           elif (Dict.get("f12") != 0):
                value = Dict.get("f12")
                Dict["f12"] = 0
                print(value)
        case 5:
            #read_int
            Dict["v0"] = int(input())
            return
        case 6 | 7:
            #read_float or read_double
            Dict["v0"] = float(input())
            return
        case 8:
            #read_string
            Dict["v0"] = input();
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