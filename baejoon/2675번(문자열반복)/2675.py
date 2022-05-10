T = int(input())
for i in range(T):
    a,b = input().split()
    a = int(a)
    word = []
    for x in range(len(b)):
        for y in range(1,a+1):
            word.append(b[x])
    print(''.join(word))