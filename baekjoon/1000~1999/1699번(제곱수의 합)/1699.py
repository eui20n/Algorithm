# 제곱수의 합
# 주어진 자연수 N을 제곱수들의 합으로 표현할 때에 그 항의 최소개수를 구해라

N = int(input())
dp = [float('inf')] * (N+1)

k = 1
num = []
while k*k <= (N+1):
    dp[k*k] = 1
    num.append(k*k)
    k+=1

for x in range(1,len(dp)):
    for y in range(len(num)):
        if num[y] > x: break
        else:
            if dp[x] > dp[x-num[y]] + dp[num[y]]:
                dp[x] = dp[x - num[y]] + dp[num[y]]

print(dp[N])
        
        
# 13 - 9 + 4
# 이중 for문을 쓰면 최악의 경우 10억개의 연산을 해야함
# 제곱수는 pass
