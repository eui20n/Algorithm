# 구간 합 구하기4
import sys

N,M = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))

result = [0] * (N+1)
result[1] = num[0]
for x in range(2,N+1):
    result[x] = result[x-1] + num[x-1]

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    print(result[j] - result[i - 1])
    
# dp 처럼함
    