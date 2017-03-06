''' Program to see how many elements in a list from two to a specified... 
	...number are divisible by any integer preceding it'''

n = 1000
numbers = range(n)
numbers.remove(0)
numbers.remove(1)

results = list()

while len(numbers) > 0:
    for val in numbers:
        results.append(val)
        for other_val in numbers:
            if other_val % val == 0:
                numbers.remove(other_val)
        break

print len(results)
    