#Program to extract numbers from lines in a file and sum them
import re
list = [] #initialize empty list
sum = 0 #initialize sum to zero
fhand = open('regex_hw_data.txt')
for line in fhand:
    numbers = re.findall('([0-9]+)', line) #extract all consecutive integers found
    list.append(numbers) #append each found number to the list
for element in list: #loop through each list element in the list containing all numbers in the file...
    for number in element: #extract through one item lists to get the numeric string...
        number = int(number) #convert numeric string to integer
        sum = sum + number #add the integer to the running total
print(sum)

    