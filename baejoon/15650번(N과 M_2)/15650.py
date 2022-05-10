# N과 M_2
# 1 부터 N까지 자연수 중에서 중복없이 M개를 고른 수열을 출력하면 됨
# N과 M_1과 동일함

N,M = map(int,input().split())

num = []

def NM(x):
    if len(num) == M:
        print(' '.join(map(str,num)))
        return
    for x in range(x,N+1):
        if x not in num:
            num.append(x)
            NM(x+1)
            num.pop()
        
NM(1)