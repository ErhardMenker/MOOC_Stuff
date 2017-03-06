fhand = open('mbox.txt')
print (fhand)
count = 0
for line in fhand :
    count = count + 1 #add a new line to the count for each line found
print ("Line count is: " + str(count)) #returns string version showing line number concatenated to string message
