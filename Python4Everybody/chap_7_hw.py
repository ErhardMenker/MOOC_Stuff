fname = input("input file name: ")
try :
	fhandle = open(fname)
except :
    print ("file does not exist")
    exit()
start_line = "X-DSPAM-Confidence:"
total = 0
count = 0 #initialize count and total to 0
for line in fhandle :
    if line.startswith(start_line) :
        count = count + 1
        value = float(line[len(start_line):])
        total = value + total #accumulates sum of the floating point values into total variable
average = total/count #produces average by dividing total by the number of value producing iterations
print ("Average spam confidence:" , average)