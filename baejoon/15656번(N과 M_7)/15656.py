# N과M_7
# 같은 수를 여러번 골라도 됨

N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
result = []

def NM():
    if len(result) == M:
        print(' '.join(map(str,result)))
        return
    for x in num:
        result.append(x)
        NM()
        result.pop()
        
NM()