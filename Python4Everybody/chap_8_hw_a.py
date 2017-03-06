t = [] #initialize empty list
fhand = open("romeo.txt")
for line in fhand : #parse each line in file
    line_read = line.split() #separate words in each line into list
    for element in line_read : #parse each element in list
        if element not in t : #if the element is not in t...
            t.append(element) #append element to t list
t.sort() #sort alphabetically
print(t)
      
   