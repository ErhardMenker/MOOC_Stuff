fout = open("testme.txt" , "w")
print (fout)
line1 = "this is how we do!\n"
fout.write(line1)
line2 = "yellow bird, yellow bird, don't fly away.\n"
fout.write(line2)
fout = open("testme.txt") #open the edited text file for parsing mode
for line in fout :
    line = line.rstrip() #eliminate "newline" white space
    if len(line) <= 20 :
        print(line , ": short line")
    else :
        print(line , ": long line")
fout.close()