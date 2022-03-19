from atexit import register
from mips import MIPS

mips = MIPS()


def add(reg1, reg2, reg3):
    mips.registers[reg1] = mips.registers[reg2] + mips.registers[reg3]
