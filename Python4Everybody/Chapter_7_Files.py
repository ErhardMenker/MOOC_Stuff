###Chapter 7: Files###

    ##Persistence
        #Until a data structure is saved to a file, the data structures are in main memory, so the content is lost when the computer is shut down.
        #Files store the data structures in secondary memory, so the files are stored more permanently and can be moved with ease.
        #A text file is a sequence of characters stored in permanent storage (such as a hard drive).
        
    ##Opening Files 
        #Opening a file communicates with the operating system to open the file by name and verify its existence.
        #A file handle is given if the requested file exists and you have the permissions to read the file.
        #A file handle is a variable that is called to perform operations on the file and read the data.
        #The file handle allows aspects of a file to be referenced without having to import all of the data.
            fhand = open("mbox.txt") #creates file handle variable which opens mbox text file in current directory
            print (fhand) #actual call to open up the filehandle to overview information
        #If the requested file does not exist in the working directory, open fails with a traceback and the contents will not open.
        #The second argument is the mode, which is an 'r' if the file is being read in and 'w' if the file is being written in through the Python script.
        
    ##Text Files and Lines
        #A text file is a sequence of lines, just as a string is a sequence of characters.
        #The special character that represents the "end of the line" is the "newline" character.
         #The newline character separates the lines of the file into lines.
        #The Python newline character is represented by a '\n', which is actually just one character.
            stuff = "Hello\nWorld"
            stuff #prints 'Hello\nWorld
            print (stuff) #returns: Hello
                          #         World
            len(stuff) #returns '11' because \n is one character
        #This means that Python will parse files and place the '\n' newline character at the end of each line.
        #Like blanks, newlines are classified as white space.
        
    ##Reading Files 
        #A for loop through a file will loop through lines, as a for loop through characters sequentially.
            fhand = open("mbox.txt") #set variable 'fhand' equal to the command to open the text file
            count = 0 #initialize count iteration variable to 0
            for line in fhand : #loop through each line in the file 
                count = count + 1 #add a value to the count variable for each iteration (line)
            print ("Line Count is " + str(count))
        #The reason the open function provides a file handle instead of opening the file...
        #...is because the file may be very large. So, the open command takes the same time for every file, regardless of size.
        #Python parses text by adding a newline character every time there is a new line in the file.
        #The "read method" reads the whole file into one string, where the string can be parsed by chapter 6 methods.
            fhand = open("mbox.txt") #set fhand as file handle referencing file open
            inp = fhand.read() #variable 'inp' inputs all fhand text into a variable name
            print (inp[:20]) #returns first 20 characters in file string
        #But the "read method" should only be used for sufficiently small files, otherwise for loop throughout the open function.
        #The "read method" will separate lines with the '\n' character
        
    ##Searching Through a File
        #Conditional code can be combined with string methods to only print certain lines.
            fhand = open("mbox.txt") #receive file hand of requested file
            for line in fhand : #loop through each line of the text file
                if line.startswith("From:") : #if the line being looped through starts with 'From:'...
                    print(line) #...then print the contents of that line 
                                #The call to print provokes an extra space because each line ends with a newline character, resulting in the double spaced output.
        #A solution to the problem of white space causing the double space is to use rstrip() method:
            for line in fhand :
                line = line.rstrip() #rename line as the same version, but with the right white space removed.
                if line.startswith("From:") :
                    print(line) 
                else :
                    print("this message shows if line starts with other line than from")
                    continue #move onto the next line, gives opportunity to exit code earlier if desired
        #The 'find' method creates useful Boolean conditions to print only certain lines in a file...
            fhand = open("mbox.txt")
            for line in fhand :
                line = line.rstrip()
                if line.find("@uct.ac.za") == -1 : #if this text is not found in the line...
                    continue #jump to the next iteration
                print (line) #else the text was found, and that line is now printed
                
    ##Using Try and Except in Conjunction with Open
        #It is possible to use the input() to ask the user for a file input:
            fname = input("enter a value here: ")
            fhand = open(fname)
            fhand = fhand.rstrip()
            count = 0 #initialize count variable to 0
            for line in count :
                if line.startswith("Subject:")
                    count = count + 1
            print('the total count for ', fname, 'is' count)
        #The above program could easily be broken when the user enters a file that is not in the directory...
        #...try and except methodology can remedy this problem:
        fname = input("enter a value here: ")
        fhand = open(fname)
        try :
            fhand = fhand.rstrip()
            count = 0 #initialize count variable to 0
            for line in count :
                if line.startswith("Subject:")
                    count = count + 1
        except :
            print("file name called", fhand, "does not exist")
            exit() #terminate the program
        print('the total count for ', fname, 'is' count)
        #The above is the protection of the open call by using try and except
        #The job of quality assurance is to try to break a program by using ridiculous inputs to ensure programmatic robusticity.
        
    ##Writing a File
        #To write a file, you have to pass w as the mode (second) argument:
            fout = open("output.txt", "w") #creates empty file called 'output.txt'
            print (fout) #file's file handle is provided
        #A new file will be created with the call to create, but if the file already existed, its content will be over written!!!
        #The "write method" inserts a new line into the text file:
            fout = open("output.txt", "w")
            line1 = "this is how we do,\n"
            fout.write(line1) #input the previous line into line 1 of the text
            line2 = "yellow bird, don't fly away,\n"
            fout.write(line2) #input the previous line into the next line of text, or line 20
            fout.close #the text file must be closed to make sure data are written to disk for when the power goes out...
        #...always call close when a file is finished to leave nothing to chance.
        #In order for the file to be parsed, it must be reopened without the second "w" argument as a "read in" file ('r')
            
    ##Debugging
        #Whitespace can be the source of error, but is problematic because whitespace is defaulted as invisible view.
        #The 'repr function' takes an object and returns a string representation of that object...
        #...for strings, whitespace characters are represented with backslash sequences.
            s = '1 2\t 3\n 4'
            print (s) #returns: 1 2  3  4
            print repr(s) #returns: '1 2\t 3\n 4'
            
        
        