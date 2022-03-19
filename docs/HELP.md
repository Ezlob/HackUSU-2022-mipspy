# Commands available in debug mode

## `run [number]`

Runs the program a specified number of lines, if no number is provided it runs until breakpoint, crash, exit, etc.

## `br [label] [[-1]]`
Create a breakpoint at a given label specified in the file.  To see a list of all labels currently available you can use `list`.  To create new breakpoints, see `create`

To see your currently set breakpoints, run `br -l`.

## `rm [label]`
Removes a label from the breakpoint list

## `dp [file]`
Dumps the contents of memory to a file for further review.  Useful for analyzing the stack and memory.
File is optional, if one is not provided the default will be used.

## `list`
Lists all availabe labels in the program

## `sp` 
Prints the current stack pointer position as well as the 4 bytes nearest to it.

## `pc`
Prints the current program counter, and the line slated to be run.

## `create [label [pos]]`

Creates a new label for the debug session.  If no position is provided the current program counter will be used.

## `help`
Prints this page.