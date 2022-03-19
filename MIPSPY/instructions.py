from atexit import register
from math import ceil
from re import M
from mips import MIPS

mips = MIPS()

# Helper function
def validate(tmp: int) -> int:
    if tmp > 2147483647:
        # Only grab 8 relevant bytes
        byte = tmp.to_bytes(ceil(tmp.bit_length() / 8), "big")[-8:]
        tmp = int.from_bytes(byte, "big")

    elif tmp < -2147483648:
        byte = tmp.to_bytes(ceil(tmp.bit_length() / 8), "big", signed=True)[-8:]
        tmp = int.from_bytes(byte, "big", signed=True)

    return tmp


# ARTHMETIC INSTRUCTIONS
# add
def add(reg1: str, reg2: str, reg3: str) -> None:
    tmp: int = mips.registers[reg2] + mips.registers[reg3]

    # "Return"
    mips.registers[reg1] = validate(tmp)


# subtract
def sub(reg1, reg2, reg3):
    mips.registers[reg1] = validate(mips.registers[reg2] - mips.registers[reg3])


# add immediate
def addi(reg1, reg2, int):
    mips.registers[reg1] = mips.registers[reg2] + int


# add unsigned
def addu(reg1, reg2, reg3):
    mips.registers[reg1] = mips.registers[reg2] + mips.registers[reg3]


# subtract unsigned
def subu(reg1, reg2, reg3):
    mips.registers[reg1] = mips.registers[reg2] - mips.registers[reg3]


# add immediate unsigned
def addiu(reg1, reg2, int):
    mips.registers[reg1] = mips.registers[reg2] + int


# multiply (without overflow)
def mul(reg1, reg2, reg3):
    mips.registers[reg1] = mips.registers[reg2] * mips.registers[reg3]


# multiply (with overflow) Dal. do
def mult(reg1, reg2):
    mips


# divide Dal. do
def div(reg1, reg2):
    mips


#LOGICAL

#and
def and_(reg1,reg2,reg3):
    mips.registers[reg1] = mips.registers[reg2] & mips.registers[reg3]

#or
def or_(reg1,reg2,reg3):
    mips.registers[reg1] = mips.registers[reg2] | mips.registers[reg3]

#and immediate
def andi_(reg1,reg2,int):
    mips.registers[reg1] = mips.registers[reg2] & int

#or immediate
def ori_ (reg1,reg2,int):
    mips.registers[reg1] = mips.registers[reg2] | int

#shift left logical
def sll_(reg1,reg2,int):
    mips.registers[reg1] = mips.registers[reg2] << int

#shift right logical
def srl_(reg1,reg2, int):
    mips.registers[reg1] = mips.registers[reg2] >> int

#DATATRANSFER

#load word
def lw(reg1, adr1):
    mips.registers[reg1] = adr1

#store word
def sw(reg1, adr1):
    adr1 = mips.registers[reg1]

#load upper immediate
def lui(reg1, const: int):
    u_bytes = const.to_bytes(2, "big")
    l_bytes = mips.registers[reg1]

#load address
def la(reg1, lab):
    mips.registers[reg1] = lab

#load immediate
def li(reg1, lab):
    lab = mips.registers[reg1]

#move from hi
def mfhi(reg1):
    mips.registers[reg1] #Dal DO

#move from low 
def mflo(reg1):
    mips.registers[reg1] #Dal DO

#move
def move(reg1,reg2):
    mips.registers[reg1] = mips.registers[reg2]

#CONDITIONAL BRANCH

#branch on equal 


