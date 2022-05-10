while True:
    a = input()
    if int(a) == 0:
        break
    b = []
    d = []
    for x in range(len(a)):
        b.append(a[x])
        d.append(a[x])
    c = []
    for _ in range(len(b)):
        c.append(b.pop())
    
    if c == d:
        print('yes')
    else:
        print('no')
    
    