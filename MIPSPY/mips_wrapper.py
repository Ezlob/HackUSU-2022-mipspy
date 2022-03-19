from typing import Callable

from .mips import MIPS


class debugger(MIPS):
    def __init__(self, file: str):
        super().__init__(file)

    def dump_data(self, filepath: str = "./datadump.txt"):
        """
        Dumps all of the data to a text file in the same directory
        """

        # Dump instructions
        with open("filepath", "w") as file:
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
            
    def debug_loop(self):
        # Commands to implement
        # run [lines, -1 to run all]
        # br [condition]
        # dump [file]
        
        while True:
            n: str = input()
            arguments = n.split()
            match arguments[0]:
                case 'run':
                    lines = int(arguments[1])
                    self.run(lines)
                case 'br':
                    pass
                case 'dump':
                    pass
                case '_':
                    print("invalid command, use h for help")