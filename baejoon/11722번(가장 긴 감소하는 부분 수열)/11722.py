# 가장 긴 감소하는 부분 수열
# 가장 긴 증가하는 부분수열과 아주 유사한 문제

N = int(input())
num = list(map(int,input().split()))

dp = [1 for _ in range(N + 1)]

for x in range(2,len(dp)):
    for y in range(x,0,-1):
        if num[x-1] >= num[y-1]:
            pass
        else:
            dp[x] = max(dp[x],dp[y]+1)
            
print(max(dp))