from typing import Dict, List, Callable
from math import ceil


class MIPS:
    instruction_set: List[List[str]]
    instr_labels: Dict[str, int]
    data_set: List[List[str]]
    data_labels: Dict[str, int]
    
    data: bytearray
    
    def __init__(self, file: str):
        from .assemble import assemble
        
        self.program_counter = 0
        self.memory: List = list()
        self.registers: Dict[str, int] = {
            "$zero": 0,
            "$0": 0,
            "$v0": 0,
            "$v1": 0,
            "$a0": 0,
            "$a1": 0,
            "$a2": 0,
            "$a3": 0,
            "$t0": 0,
            "$t1": 0,
            "$t2": 0,
            "$t3": 0,
            "$t4": 0,
            "$t5": 0,
            "$t6": 0,
            "$t7": 0,
            "$t8": 0,
            "$t9": 0,
            "$s0": 0,
            "$s1": 0,
            "$s2": 0,
            "$s3": 0,
            "$s4": 0,
            "$s5": 0,
            "$s6": 0,
            "$s7": 0,
            "$ra": 0,
            "$gp": 0,
            "$sp": 0,
            "$fp": 0,
            "$ra": 0,
            "$hi": 0,
            "$lo": 0
        }
        # Load instructions
        self.instruction_set, self.instr_labels, self.data_set, self.data_labels = assemble(file)

        # Load Data into memory
        self.data_ptr = 0
        self.data = bytearray()
        
        for key, val in self.data_labels.items():
            command: List[str, str] = self.data_set[val]
            
            byte: bytearray
            if (command[0] == ".word"):
                # convert int to bytes
                byte = bytearray(int(command[1]).to_bytes(4, 'big'))
                    
            elif (command[0] == ".asciiz"):
                command[1] = command[1].replace('"', '')
                byte = bytearray(command[1] + '\0', 'utf-8')
            
            # Add to data array 
            self.data += byte
            
            # update data label
            self.data_labels[key] = self.data_ptr
            self.data_ptr = self.data_ptr + len(byte) - 1

        # Update %sp
        self.registers['$sp'] = len(self.data) - 1

    def run(self):
        while True:
            instruction = self.instruction_set[self.program_counter]
            # Get instruction to run
            cmd: Callable = self.get_instruction(instruction[0])
                # Run instruction

            cmd(self, *instruction[1:])

            # increment pc by 1
            self.program_counter += 1

    def get_instruction(self, cmd: str):
        from .syscalls import syscall
        from . import instructions
        
        match cmd:
            case "add":
                return instructions.add
            case "sub":
                return instructions.sub
            case "addi":
                return instructions.addi
            case "addu":
                return instructions.addu
            case "subu":
                return instructions.subu
            case "addiu":
                return instructions.addiu
            case "mul":
                return instructions.mul
            case "mult":
                return instructions.mult
            case "and_":
                return instructions.and_
            case "or":
                return instructions.or_
            case "andi":
                return instructions.ori_
            case "sll":
                return instructions.sll_
            case "srl":
                return instructions.srl_
            case "lw":
                return instructions.lw
            case "sw":
                return instructions.sw
            case "lui":
                return instructions.lui
            case "la":
                return instructions.la
            case "li":
                return instructions.li
            case "mfhi":
                return instructions.mfhi
            case "mflo":
                return instructions.mflo
            case "move":
                return instructions.move
            case "beq":
                return instructions.beq
            case "bne":
                return instructions.bne
            case "bgt":
                return instructions.bgt
            case "blt":
                return instructions.blt
            case "ble":
                return instructions.ble
            case "slt":
                return instructions.slt
            case "slti":
                return instructions.slti
            case "j":
                return instructions.j
            case "jr":
                return instructions.jr
            case "jal":
                return instructions.jal
            case "jalr":
                return instructions.jalr
            case "syscall":
                return syscall
            case _:
                raise NotImplementedError
            
            