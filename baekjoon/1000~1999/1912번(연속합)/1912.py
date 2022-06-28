# 연속합

N = int(input())
num = list(map(int,input().split()))

a = min(num)

dp = [a for _ in range(N+1)]
dp[1] = num[0]

for x in range(2,len(dp)):
    dp[x] = max(dp[x-1]+num[x-1],num[x-1])


print(max(dp))