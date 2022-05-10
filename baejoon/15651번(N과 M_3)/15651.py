# N과M_3
# 중복 허용

N,M = map(int,input().split())
num = []

def NM():
    if len(num) == M:
        print(' '.join(map(str,num)))
        return
    for x in range(1,N+1):
        num.append(x)
        NM()
        num.pop()

NM()
