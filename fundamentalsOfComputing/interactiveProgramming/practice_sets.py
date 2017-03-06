# use set to count how many unique numbers occur in loop

def next(x):
    return (x ** 2 + 79) % 997

count = set([])
x = 1
for i in range(1000):
    #print x
    count.add(x)
    x = next(x)
    
print len(count)