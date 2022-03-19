# MIPSPY 
## *A MIPS simulator / debugger built in python*

MIPSPY aims to simplyfy the running, debugging, and creation of simple mips scripts using a lightweight terminal design, rather than a burdensome IDE like some other clients do.

## FEATURES

### TERMINAL BASED GUI
While it may not be the prettiest design, or the most user intuitive, having a lightweight debugger that can be easily used alongside your favorite editors and IDE's is the perfect choice.  Much better than those clunky windows based solutions like mars.

The ease of use of simple commands and clear instructions will speed up any mips project you'd need.

### SAVE STATES
We took one of the best parts of video game emulation and brought it into our debugger.  Simply save your postion by creating a checkpoint, and load it back when you start to debug again! You can even save multiple to juggle between scenarios.

### Simple breakpoints, labels, and memory viewing
No opening a window, or searching google for how to's, just type br and you're good to go!

We've also simplified the PC to match up directly with each command, so now you know that PC 3 is always line 3.


## *DESIGNING PROCESS*

- We aimed to create a tool that could be utilized in the debugging process for mips code

- We recognized that this program had many different moving parts tha were seperate but all worked together cohesivley to produce what we needed

	- Knowing this, we split the workload but maintained heavy communication and teamwork to make code that all worked together in the end

- Once our seperate bits were completed, we then worked as a team to merge them all together, collaborating on debugging and tests to refine the capabilities of our program

- After almost all the bugs were smoothed out we split into two groups: one to continue smoothing the bugs out and one to begin developing the UI for our program

- The UI group spent several hours learning a new language to code the UI in but then after careful consideration realized that building a wrapper that allowed other command line commands to be entered and processed would work for the vision we had

- Once the code's bugs were smoothed out and we could execute simple programs like factorials, addition, string printing, and others, we connected the UI and the code together to create a usable user interface for running mips code.

## Differences between hardware and our solution
- Our program counter is stored line by line, so PC 1 clearly translates to line 1, making it easier to understand.  

- Being implemented in this way allows us to in the future implement save states to be able to execute the code backwards, undoing what was done previously.



