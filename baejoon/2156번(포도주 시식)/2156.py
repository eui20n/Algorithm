# 포도주 시식
# 계단 오르기와 비슷한 유형의 문제
# 연속으로 놓여 있는 3잔을 모두 마실 수 없음
# 이때 가장 포도주를 가장 많이 마실 수 있는 양을 출력하면 됨

N = int(input())
wine = []
for _ in range(N):
    a = int(input())
    wine.append(a)
    
dp = [0 for _ in range(N+1)]
dp[1] = wine[0]
if len(dp) > 2:
    dp[2] = wine[0] + wine[1]

for x in range(3,len(dp)):
    dp[x] = max(dp[x-2] + wine[x-1], wine[x-1] + wine[x-2] + dp[x-3],wine[x-1] + wine[x-2] + dp[x-4])


print(max(dp))

