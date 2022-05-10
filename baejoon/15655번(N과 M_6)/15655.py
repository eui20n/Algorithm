# N과M_6
# 서로 다른 수가 주어짐
# 수열을 고르는데 그 수열이 오름차순이여야함

N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
result = []

def NM(x):
    if len(result) == M:
        print(' '.join(map(str,result)))
        return
    for x in range(x,len(num)):
        if num[x] not in result:
            result.append(num[x])
            NM(x)
            result.pop()
            
NM(0)