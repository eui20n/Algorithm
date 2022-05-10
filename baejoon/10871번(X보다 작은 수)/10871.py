# X보다 작은 수
# 그냥 풀어 보는 문제
N,M = map(int,input().split())
num = list(map(int,input().split()))
for x in num:
    if M > x:
        print(x,end = ' ')