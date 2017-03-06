fhandle = open('mbox-short.txt')
maximum_value = None
name_dictionary = dict() #initialize an empty dictionary

for line in fhandle :
    if line.startswith("From ") :
        line = line.split() #split each line into a list of word elements
        name = line[1] #email address extracted from list
        name_dictionary[name] = name_dictionary.get(name , 0) + 1 #add an instance of that email to the dictionary
print(name_dictionary)

for key , value in name_dictionary.items() :
    print(key , value)
    if value > maximum_value or maximum_value is None :
        maximum_value = value 
        maximum_key = key
print (maximum_key , "appears :" , maximum_value , "times")

print "this sexecutes san parenthesis!"
text = input("does this show up?")