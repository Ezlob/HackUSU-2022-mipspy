from typing import Dict

from typing import List, Dict

class MIPS():
    
    memory: List
    registers: Dict
    
    def __init__(self):
        self.memory = List()
        self.registers = {}
        