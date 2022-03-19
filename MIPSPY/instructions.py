from atexit import register
from math import ceil
from re import M
from mips import MIPS

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
def add(mips: MIPS, reg1: str, reg2: str, reg3: str) -> None:
    tmp: int = mips.registers[reg2] + mips.registers[reg3]

    # "Return"
    mips.registers[reg1] = validate(tmp)


# subtract
def sub(mips: MIPS, reg1, reg2, reg3):
    mips.registers[reg1] = validate(mips.registers[reg2] - mips.registers[reg3])


# add immediate
def addi(mips: MIPS, reg1, reg2, imd):
    mips.registers[reg1] = mips.registers[reg2] + int(imd)


# add unsigned
def addu(mips: MIPS, reg1, reg2, reg3):
    mips.registers[reg1] = mips.registers[reg2] + mips.registers[reg3]


# subtract unsigned
def subu(mips: MIPS, mips: MIPS, reg1, reg2, reg3):
    mips.registers[reg1] = mips.registers[reg2] - mips.registers[reg3]


# add immediate unsigned
def addiu(mips: MIPS, reg1, reg2, imd):
    mips.registers[reg1] = mips.registers[reg2] + int(imd)


# multiply (without overflow)
def mul(mips: MIPS, reg1, reg2, reg3):
    mips.registers[reg1] = mips.registers[reg2] * mips.registers[reg3]


# multiply (with overflow) Dal. do
def mult(mips: MIPS, reg1, reg2):
    mips


# divide Dal. do
def div(mips: MIPS, reg1, reg2):
    mips


# LOGICAL

# and
def and_(mips: MIPS, reg1, reg2, reg3):
    mips.registers[reg1] = mips.registers[reg2] & mips.registers[reg3]


# or
def or_(mips: MIPS, reg1, reg2, reg3):
    mips.registers[reg1] = mips.registers[reg2] | mips.registers[reg3]


# and immediate
def andi_(mips: MIPS, reg1, reg2, imd):
    mips.registers[reg1] = mips.registers[reg2] & int(imd)


# or immediate
def ori_(mips: MIPS, reg1, reg2, imd):
    mips.registers[reg1] = mips.registers[reg2] | int(imd)


# shift left logical
def sll_(mips: MIPS, reg1, reg2, imd):
    mips.registers[reg1] = mips.registers[reg2] << int(imd)


# shift right logical
def srl_(mips: MIPS, reg1, reg2, imd):
    mips.registers[reg1] = mips.registers[reg2] >> int(imd)


# DATATRANSFER

# load word
def lw(mips: MIPS, reg1, adr1):
    mips.registers[reg1] = adr1


# store word
def sw(mips: MIPS, reg1, adr1):
    adr1 = mips.registers[reg1]


# load upper immediate
def lui(mips: MIPS, reg1, const: int):
    u_bytes = const.to_bytes(2, "big")
    l_bytes = mips.registers[reg1]


# load address
def la(mips: MIPS, reg1, lab):
    mips.registers[reg1] = lab


# load immediate
def li(mips: MIPS, reg1, lab):
    lab = mips.registers[reg1]


# move from hi
def mfhi(mips: MIPS, reg1):
    mips.registers[reg1]  # Dal DO


# move from low
def mflo(mips: MIPS, reg1):
    mips.registers[reg1]  # Dal DO


# move
def move(mips: MIPS, reg1, reg2):
    mips.registers[reg1] = mips.registers[reg2]


# CONDITIONAL BRANCH

# branch on equal
def beg(mips: MIPS, reg1, reg2, imd):
    if reg1 == reg2:
        mips.program_counter += int(imd)


# branch on not equal
def dne(mips: MIPS, reg1, reg2, imd):
    if reg1 != reg2:
        mips.program_counter += int(imd)


# branch on greater than
def bgt(mips: MIPS, reg1, reg2, imd):
    if reg1 > reg2:
        mips.program_counter += int(imd)


# branch on greater than or equal
def bge(mips: MIPS, reg1, reg2, imd):
    if reg1 >= reg2:
        mips.program_counter += int(imd)


# branch on less than
def blt(mips: MIPS, reg1, reg2, imd):
    if reg1 < reg2:
        mips.program_counter += int(imd)


# branch on less than or equal
def ble(mips: MIPS, reg1, reg2, imd):
    if reg1 <= reg2:
        mips.program_counter += int(imd)


# COMPARISON

# set on less than
def slt(mips: MIPS, reg1, reg2, reg3):
    if reg2 == reg3:
        mips.registers[reg1] = 1
    else:
        mips.registers[reg1] = 0


# set on less than immediate
def slti(mips: MIPS, reg1, reg2, imd):
    if reg2 == int(imd):
        mips.registers[reg1] = 1
    else:
        mips.registers[reg1] = 0


# UNCONDITIONAL JUMP

# jump
def j(mips: MIPS, imd):
    mips.program_counter += int(imd) // 4


# jump register
def jr(mips: MIPS, reg1):
    mips.program_counter += mips.registers[reg1] // 4


# jump and link
def jal(mips: MIPS, imd):
    # Dal do
    mips.program_counter += int(imd)
