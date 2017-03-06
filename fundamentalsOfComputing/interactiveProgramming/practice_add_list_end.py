list = [0, 1]
n = 40

for i in range(n):
    val = list[-1] + list[-2]
    list.append(val)
    
print(list[-1])
  