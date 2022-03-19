from locale import ABMON_10


def syscall(v):
    match v:
        case 1 | 2 | 3 |4:
           #print cases
           if(Dict.get("v0") != 0) :
               value = Dict.get("v0")
               Dict["v0"] = 0
               print(value)
           elif (Dict.get("f12") != 0):
                value = Dict.get("f12")
                Dict["f12"] = 0
                print(value)
        case 5:

            return
        case 6:
            return
        case 7:
            return
        case 8:
            return
        case 9:
            return
        case 10:
            return
        case 11:
            return
        case 12:
            return
        case 13:
            return
        case 14:
            return
        case 15:
            return
        case 16:
            return
        case 17:
            return