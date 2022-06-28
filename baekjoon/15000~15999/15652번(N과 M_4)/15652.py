# N과M_4
# 수열이 내림차순이여야함

N,M = map(int,input().split())
num = []

def NM():
    sort_num = []
    if len(num) == M:
        sort_num = sorted(num)
        if sort_num == num:
            print(' '.join(map(str,num)))
        return
    for x in range(1,N+1):
        num.append(x)
        NM()
        num.pop()
            
NM()