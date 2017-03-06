fname = input("Input file name: ")
fhandle = open(fname) #create file handle
d = dict() #initialize an empty dictionary
for iterated_line in fhandle:
    line = iterated_line #rename iterated line to avoid computing errors
    if line.startswith("From "):
        line = line.split() #split the iterated line into a list of space-delimited words
        word = line[5] #extract the hour-minute-second text 
        word = word.split(":") #split the hour, minute, second apart using a colon delimiter
        hour = word[0] #extract the hour from the above text
        d[hour] = d.get(hour, 0) + 1
print(d) #print the completed dictionary for a given file. Produces 'hour-count' 'key-value' pairs

#sort from smallest to largest key (by hour):
d = d.items() #convert dictionary into a list of key-value pair tuples.
d.sort() #sorts and prints from smallest to largest key
print("sort from smallest to largest value of the key (hour):")
for key, value in d:
    print key, value

#sort from smallest to largest key (by count):
t = list() #initiate empty list to append value-key pairs onto. 
for key, value in d: #for a key-value pair in the dictionary...
    t.append((value, key)) #...append as a value-key pair to allow alphabetical sorting by value, primarily
t.sort() #sort each tuple element in the list by the value (count), only sorting by the hour if the value for multiple key-value pairs is tied.
print("sort from smallest to largest value of the value (count):")
for value, key in t:
    print value, key    

    
    