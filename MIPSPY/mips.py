from typing import Dict, List, Tuple
from assemble import assembler
from math import ceil


class MIPS:
    def __init__(self, file: str):
        
        self.program_counter = 0
        self.memory: List = List()
        self.registers: Dict[str, int] = {
            "$0": 0,
            "v0": 0,
            "v1": 0,
            "a0": 0,
            "a1": 0,
            "a2": 0,
            "a3": 0,
            "t0": 0,
            "t1": 0,
            "t2": 0,
            "t3": 0,
            "t4": 0,
            "t5": 0,
            "t6": 0,
            "t7": 0,
            "t8": 0,
            "t9": 0,
            "s0": 0,
            "s1": 0,
            "s2": 0,
            "s3": 0,
            "s4": 0,
            "s5": 0,
            "s6": 0,
            "s7": 0,
            "ra": 0,
            "gp": 0,
            "sp": 0,
            "fp": 0,
            "ra": 0,
        }

        self.labels: Dict = assembler(file)

    def load_data(self, instructions: List[Tuple], labels: Dict):
        for instr in instructions:
            # Get instruction to run
            cmd: function = get_instruction(instr.pop(0))

            # Run instruction
            cmd(*instr)


# DATATYPES TO FOLLOW
