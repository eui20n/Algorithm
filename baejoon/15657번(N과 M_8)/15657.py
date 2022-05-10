# N과M_8
# 수열을 여러번 골라도 됨
# 하지만 내림차순이여야함

N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
result = []

def NM():
    if len(result) == M:
        result_sort = []
        result_sort = sorted(result)
        if result_sort == result:
            print(' '.join(map(str,result)))
        return
    for x in num:
        result.append(x)
        NM()
        result.pop()

NM()