### Chapter 16: Automating Common Tasks on Your Computer ###

## Introduction
# Python can go through all the directories and folders of a computer and read in all corresponding files.
# Files are organized into directories (folders).
# Simple Python scripts can make short work of simple tasks that must be run across many files spread about many directories!
# All directories on an OS can be walked to via os.walk and a for loop (like open on text files or urllib for the web).

## File Names and Paths
# Every running program has a "current directory" which is the default directory for most operations.
# The os module provides functions for working with files and directories.
# os.getcwd returns the name of the current directory:

# fetch operating system "os" module
import os
cwd = os.getcwd()
print("cwd is: ", cwd) #returns where this file was run from (visible from command line)

# A string (cwd included) that identifies a file is a path.
# A relative path is navigated from the current directory.
# An absolute path starts from the topmost directory in the file system.
# To find the absolute path to a file, use: os.path.abspath() (with a file input).

import os
abspath = os.path.abspath('chapter_16_file_automation.py')
print ("absolute path is ", abspath) # not found by reference to CWD

# os.path.exists() checks whether the inputted file or directory exists, assuming the CWD holds (relative path from CWD assumed)

import os
test = os.path.exists('geodump.py') # checks in CWD
print(test) # returns: True

# Conditioned on existence, os.path.isdir() checks whether the input is a directory.

import os
dir_test = os.path.isdir('geodump.py')
print(dir_test) # returns false, this Python file is not a folder!

# Conditioned on existence, os.path.isfile() checks whether input is a file

import os
file_test = os.path.isfile('geodump.py')
print(file_test) # returns: True

# Calling os.walk() will start from the inputted directory and move up, returning...
# ...a three element tuple of the directory name, list of subdirectories within the folder, and a list of files within the directory, respectively.
# In a for loop used with os.walk(), subdirectories of the inputted directory are automatically crawled.

import os
count = 0
# '.' indicates to start at the CWD and then work downward, going further into relative subdirectories
# for iteration, return the directory name and all directories/files, respectively in a tuple
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            count += 1
# prints the sum of text files found within the inputted directory and all child directories from this location
print('Files:', count)

# Program to crawl inputted directory and all subdirectories and print the text files and their size

import os
# import join, a sub-module within the os module
from os.path import join
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            # concatenate the file to its directory (starting from inputted directory)...
            # ...note that join is a smarter version of string concatenation
            thefile = os.path.join(dirname, filename)
            # get size method says how many lines the file is (possible indicator of which files should be deleted)
            print(os.path.getsize(thefile), thefile)
            
            # os.remove() can be used to eliminate bad directories/files (and is presumably VERY DANGEROUS).
            
            ## Command-line arguments
            # Instead of using input() to enter information in the command line, we can place additional strings after the...
            # ...Python file and access those command line arguments in our Python program.
            
import sys
# The contents of sys.argv are a list of strings where the first string is the name of the Python program and...
# ...the remaining strings are the arguments on the command line after the Python file.
print('Count:', len(sys.argv))
print('Type:', type(sys.argv))
for arg in sys.argv:
    print('Argument:', arg)

## Pipes
# Most operating systems provide a command-line interface, called a shell.
# Shells provide commands to navigate the file system and launch applications.
# Example: Unix allows the changing of directories with cd and to display contents of the directory with ls.
# Any program that you can launch from the shell can be launched from Python using a pipe.
# A pipe is an object that represents a running process.
# Pipes can be opened using os.popen() where the input is the command line argument.

# Example: ls -l displays the contents fo the current directory in long format
# Python pipe for 'ls -l' using os.popen():
cmd = 'ls -l'
fp = os.popen(cmd)
# read everything:
res = fp.read()
# close pipe:
stat = fp.close()




