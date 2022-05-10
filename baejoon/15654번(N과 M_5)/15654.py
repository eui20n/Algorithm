# N과M_5
# 서로 다른 수의 수열을 출력하면 됨

N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
result = []

def NM():
    if len(result) == M:
        print(' '.join(map(str,result)))
        return
    for x in num:
        if x not in result:
            result.append(x)
            NM()
            result.pop()
            
NM()