# 2 x n 타일링
# 2 x n 직사각형에 1 x 2, 2 x 1 타일로 채우는 방법의 수를 구하는 프로그램을 작성해라
# 입력은 n

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
dp[3] = 3
for x in range(4,len(dp)):
    dp[x] = dp[x-1] + dp[x-2]
    

print(dp[n]%10007)

# 1 - 1
# 2 - 2
# 3 - 3
# 4 - 5