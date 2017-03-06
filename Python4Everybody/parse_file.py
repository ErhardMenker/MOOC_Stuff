fhand = open("mbox.txt")
for line in fhand :
    line = line.rstrip() #clear pesky rightward white space to avoid double spacing
    if line.startswith("From:") : 
        print(line) #print line if line starts with the method input
    else : 
        print("could not be found :(") #print message if the if condition does not hold