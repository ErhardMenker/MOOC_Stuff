###Chapter One: Why We Program###

##Programming motivation
	#Programming computers is used to make our lives easier, but can only be done effectively if proper syntax is used.
	#Users see computers as a set of tools such as spreadsheets, but programmers understand the underlying  mechanics that make such processes possible.
	#A program is a sequence of stored instructions, or code.	
	
##Computer hardware overview
	#The central processing unit (CPU) is the “brain” of the computer, which calculates processes quickly when instructed.
	#The main memory is the random access memory (RAM) which stores the high speed instructions and data (lost on reboot).
	#The secondary memory is disk space which is slower than the main memory but is also more permanent (lasts until deleted).
	#The input and output devices connect the computer to outside components (such as an Ethernet cable).
	
##Python as a language
	#Python is the language of the Python Interpreter.
	#An individual who can speak Python is a Pythonista.
	#Python was invented by Guido van Rosum.
	#The title Python is a reference to Monty Python.
	#Syntax error occurs when improper code is executed that the CPU does not recognize, but it is easier for humans to learn Python than for Python to learn English!
	#Python is free and transitioning from its second to its third edition.
	#Python is a high level language because it is designed for humans to read and write, and thus has a defining source code.
	#A low level language is what the CPU actually executes as a set of understandable machine code. The CPU is able to convert high level Python (and other high level language) code into computer understandable (machine) code before executing.

##Basic Python program classifications
	#A variable is text that has a value assigned to it.
	#An operator executes an operation on a variable(s), such as equal or summation.
	#A constant is a numerical value.
	#A reserved word has special meaning to Python such as “for” or “print,” and cannot be used to store other variable values because it refers to a built in command.

##Interpreter and Compiler
	#An interpreter reads the source code of a program and interprets it on the fly, line by line, waiting for more code. The Python prompt that opens is an interpreter, as is running code step by step through the non-script “command prompt” of a language.
	#A compiler needs to run all of the program’s code at once. This includes saving a set of programming instructions (script) and running that Python program through the window’s command line.
	#A script is the entirety of the program’s code written in an adjustable format. Scripts should be written in Notepad ++, and have .py added immediately to the end of the scripts name.

##Generic Programming Terms Across All Languages
	#Inputs involve importing data from the outside world. Examples include using results from a CSV or a sensor like a GPS.
	#Outputs display the results of a program or store them to a file or device (such as the GPS).
	#Sequential execution performs statements one after another in the order encountered in the script.
	#Conditional execution performs a set of statements in order, so long as they satisfy stated conditions.
	#Repeated execution performs a set of instructions repeatedly, usually with some variation.
	#Reuse is a set of programming instructions that are saved because they can be used again for data in another program (like a program that you exec in EViews).

##Categories of Programming Errors
	#Syntax errors are flaws in the code that violate Python’s “grammar” conventions. These usually occur with beginning programmers. Python will point to the line where it detected the syntax error, but the flaw in the code might have actually occurred earlier.
	#To parse a code means to examine a program’s code and analyze its syntactic structure.
	#Logic errors occur when a program has valid syntax, but errors in the ordering of the statements or how the statements relate to one another results in a program that does not convey what the programmer wishes.
	#Semantic errors occur when a program is syntactically perfect and executes without being stopped, but the program does not execute as the programmer wished (meaning the program semantics are improper). For example, the data included in a file may be coerced incorrectly.

##Installing Python and Understanding its Supporting Tools (Command Line and Notepad ++)
	#Python can be downloaded for free from python.org.
	#Python can be written using Notepad ++, with selecting Python as the default language. This allows Notepad ++ to use predictive text in Python style. Once the Python code is written, save it in the proper folder with adding “.py” at the end of the file name. 
	#Omit spaces in the program’s name.
	#Code written with Notepad ++ with the Python language can be executed by opening the command line by entering “cmd” in the start menu.
	#Change the directory in the command line to the one where the Python program lives.
	#Moving up a level in the command line is done by executing cd ..
	#To go down in the directory, execute cd <dirName> where dirName is the name of the folder existing below the directory the command line currently is on.
	#Once the command line is in the most local directory containing the desired Python file, the file can be executed by entering the name of the file (making sure to include .py at the end). The substance of the file’s execution will occur immediately in the command line.

