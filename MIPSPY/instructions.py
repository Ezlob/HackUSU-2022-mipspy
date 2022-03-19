from atexit import register
from re import M
from mips import MIPS

mips = MIPS()

#ARTHMETIC INSTRUCTIONS
#add
def add(reg1, reg2, reg3):
    mips.registers[reg1] = mips.registers[reg2] + mips.registers[reg3]
#subtract
def sub(reg1,reg2,reg3):
    mips.registers[reg1] = mips.registers[reg2] - mips.registers[reg3]
#add immediate
def addi(reg1,reg2,int):
    mips.registers[reg1] = mips.registers[reg2] + int
#add unsigned
def addu(reg1,reg2,reg3):
    mips.registers[reg1] = mips.registers[reg2] + mips.registers[reg3]
#subtract unsigned
def subu(reg1,reg2,reg3):
    mips.registers[reg1] = mips.registers[reg2]- mips.registers[reg3]
#add immediate unsigned
def addiu(reg1,reg2,int):
    mips.registers[reg1] = mips.registers[reg2] +int
#multiply (without overflow)
def mul(reg1,reg2,reg3):
    mips.registers[reg1]= mips.registers[reg2] * mips.registers[reg3]
#multiply (with overflow) Dal. do
def mult(reg1,reg2):
    mips
#divide Dal. do
def div(reg1,reg2):
    mips

#LOGICAL
#and
def _and(reg1,reg2,reg3):
    mips.registers[reg1] = mips.registers[reg2] & mips.registers[reg3]
#or
def _or(reg1,reg2,reg3):
    mips.registers[reg1] = mips.registers[reg2] | mips.registers[reg3]
#and immediate
def _andi(reg1,reg2,int):
    mips.registers[reg1] = mips.registers[reg2] & int
#or immediate
def _ori (reg1,reg2,int):
    mips.registers[reg1] = mips.registers[reg2] | int
#shift left logical
def _sll(reg1,reg2,int):
    mips.registers[reg1] = mips.registers[reg2] << int