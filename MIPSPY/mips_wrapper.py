from ast import arg
import pickle
from typing import Callable, Dict, List
from os import get_terminal_size

from .mips import MIPS


class debugger(MIPS):
    cp_data : List
    cp_instr : List
    cp_reg : List
    cp_pc : int
    cp_labels : List
    
    
    def __init__(self, file: str):
        self.breakpoints: Dict = dict()
        super().__init__(file)

    def dump_data(self, filepath: str = "./datadump.txt"):
        """
        Dumps all of the data to a text file in the same directory
        """

        # Dump instructions
        with open(filepath, "w") as file:
            file.write("Instruction set\n")
            for num, line in enumerate(self.instruction_set):
                file.write(f"{num} : {line}\n")
            file.write("\n\n\n")
            file.write("Data set\n")
            for num, line in enumerate(self.data_set):
                file.write(f"{num} : {line}\n")
            file.write("\n\n\n")
            file.write("Instruction labels\n")
            for num, line in enumerate(self.data_labels):
                file.write(f"{num} : {line}\n")
            file.write("\n\n\n")
            file.write("Data labels\n")
            for num, line in enumerate(self.instr_labels):
                file.write(f"{num} : {line}\n")

    def run(self, lines_to_run: int):
        while lines_to_run != 0:
            
            instruction = self.instruction_set[self.program_counter]
            # Get instruction to run
            cmd: Callable = self.get_instruction(instruction[0])
            # Run instruction

            cmd(self, *instruction[1:])

            # increment pc by 1
            self.program_counter += 1
            lines_to_run -= 1
            
            # check for breakpoint first
            if self.program_counter in self.breakpoints:
                print(f"-> stopped at {self.breakpoints[self.program_counter]}, press run to continue")
                break
            
    def debug_loop(self):
        # Commands to implement
        # run [lines, -1 to run all]
        # br [condition]
        # dump [file]
        print("-! `help` to see a list of all commands")
        try:
            while True:
                print("-> ", end="")
                n: str = input()
                arguments = n.split()
                if len(arguments) == 0:
                    continue
                match arguments[0]:
                    case 'run':
                        if len(arguments) == 2:
                            self.run(int(arguments[1]))
                        else:
                            self.run(-1)
                            
                    case 'br':
                        # BR allows a user to set a breakpoint at a pre-existing label
                        if '-l' in arguments[1:]:
                            arguments.remove('-l')
                            for bk, bv in self.breakpoints.items():
                                print(f"-| {bv} : {bk}")
                        self.bp_set(arguments[1:])
                    case 'rm':
                        for ele in arguments[1:]:
                            self.breakpoints.pop(self.instr_labels[ele])
                            
                    case 'dp':
                        if len(arguments) >= 2:
                            self.dump_data(arguments[1])
                        else: 
                            self.dump_data()
                    case 'list':
                        for key, val in self.instr_labels.items():
                            print(f"-| {key} : {val}")
                    # Prints the current stackk pointer and a given word
                    case 'sp':
                        sp = self.registers['$sp']
                        word = int.from_bytes(self.data[sp - 3: sp], "big", signed=True)
                        print(f"-| {sp}: {word}")
                    # Prints the current program counter & line
                    case 'pc':
                        line = " ".join(self.instruction_set[self.program_counter])
                        print(f"-| {self.program_counter} : {line}")
                        
                    # create [name, [pos]]
                    # position can be omitted to create at current pointer
                    case 'create':
                        if len(arguments[1:]) == 2:
                            self.instr_labels.update({arguments[1]: arguments[2]})
                        elif len(arguments[1:]) == 1:
                            self.instr_labels.update({arguments[1]: self.program_counter})
                        else:
                            print("-| Error: Invalid parameters passed:\n"
                                  "-| Follow the template `create name *pos*`")
                    case 'cp' | 'checkpoint':
                        if len(arguments[1:]) == 0:
                            self.checkpoint(f"checkpoint: {self.program_counter}")
                        else:
                            self.checkpoint(arguments[1])
                    case 'load':
                        if len(arguments[1:]) != 1:
                            print("-| invalid command, use h for help")
                        else:
                            self.load_checkpoint(arguments[1])
                            
                    case 'help':
                        self.help()   
                         
                    case '_':
                        print("-| invalid command, use h for help")
                        
        except KeyboardInterrupt:
            print("\n-| Exiting program...")
    
    def checkpoint(self, filename):
        self.cp_data = self.data_set.copy()
        self.cp_instr = self.instruction_set.copy()
        self.cp_reg = self.registers.copy()
        self.cp_pc = self.program_counter
        self.cp_labels = self.instr_labels.copy()
        tt = (self.cp_data, self.cp_instr, self.cp_reg, self.cp_pc, self.instr_labels)
        
        # Save CP to file
        with open(filename + '.pickle', 'wb') as f:
            pickle.dump(tt, file=f)

    def load_checkpoint(self, filename):
        
        # Load pickle into class
        with open(filename + '.pickle', 'rb') as file:
            tt = pickle.load(file) 
            self.data_set = tt[0].copy()
            self.instruction_set = tt[1].copy()
            self.registers = tt[2].copy()
            self.program_counter = tt[3] 
            self.instr_labels = tt[4].copy()
        
        
    def bp_set(self, arguments: List[str]):
        for arg in arguments:
            if arg in self.instr_labels:
                self.breakpoints.update({self.instr_labels[arg] : arg})
            else:
                print(f"-| ERROR: Invalid tag, {arg} ignored")
                
    def help(self):
        # Prints the help file attached
        size, _ = get_terminal_size()
        with open("docs/HELP.md") as file:
            for line in file:
                if size > len(line) - 3:
                    print("-| " + line, end="")
                else:
                    while line:
                        print("-| " + line[:size - 3])
                        line = line[size - 3:]
                        if len(line) < size:
                            print("-| " + line, end="")
                            break
            print()
                        