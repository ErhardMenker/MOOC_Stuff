count = 0
def f(string):
    global count
    for word in string:
        if word == 'l':
            count += 1
    return count

print (f('1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1'))
