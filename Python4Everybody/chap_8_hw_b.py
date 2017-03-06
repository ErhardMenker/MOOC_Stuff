File_Name = input("Input File Name :")
try :
    fhandle = open(File_Name)
except :
    print("erroneous file name")
count = 0
for lines in fhandle : #iterate through each line in text file
    word_list = lines.split() #partition each line into a list of all words
    try :
        if word_list[0] == "From" : #if zeroeth entry in list is 'From'...
            desired_entry = word_list[1] #extract email address
            print(desired_entry)
            count = count + 1 #keep count of email addresses
    except :
        continue
output_message = "final output is: " + str(count)
print(output_message)

