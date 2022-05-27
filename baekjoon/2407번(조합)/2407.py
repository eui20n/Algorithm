# 조합
# nCm 출력하기

n,m = map(int,input().split())

dp = [[0]*101 for _ in range(101)]

for x in range(1,101):
    dp[x][0] = 1
    dp[x][x] = 1

# 파스칼의 삼각형
for x in range(2,101):
    for y in range(1,x):
        dp[x][y] = dp[x-1][y-1] + dp[x-1][y]

print(dp[n][m])