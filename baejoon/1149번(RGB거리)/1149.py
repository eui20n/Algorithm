# RGB 거리
# RGB거리에 집이 N개 있고, 1번 부터 N번 집까지 있다
# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다
# 각각의 집에 비용이 있을때 규칙에 따라 칠하는 비용의 최솟값을 구해라
# 1. 1번 집의 색은 2번 집의 색과 같지 않다
# 2. N번 집의 색은 N-1번 집과 같지 않다
# 3. i(2 <= i <= N-1)번 집의 색은 i-1,i+1번 집의 색과 같지 않다
# 입력은 첫줄에 집 수, 두번째 줄부터 집에 대한 RGB비용이 있다
# 출력은 집을 칠하는 비용의 최솟값이다

T = int(input())
cost = [list(map(int,input().split()))for _ in range(T)]

dp = [[0]*3 for _ in range(T+1)]
dp[1][0] = cost[0][0]
dp[1][1] = cost[0][1]
dp[1][2] = cost[0][2]

for x in range(2,T+1):
    dp[x][0] = min(dp[x-1][1] + cost[x-1][0],dp[x-1][2] + cost[x-1][0])
    dp[x][1] = min(dp[x-1][2] + cost[x-1][1],dp[x-1][0] + cost[x-1][1])
    dp[x][2] = min(dp[x-1][1] + cost[x-1][2],dp[x-1][0] + cost[x-1][2])

print(min(dp[T]))