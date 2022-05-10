# 파도반 수열
# 삼각형이 붙여진 형태의 수열을 만들면 됨
# 그 수열을 파도반 수열이라고 하는듯

T = int(input())
for _ in range(T):
    num = int(input())
    dp = [0,1,1,1,2,2]
    if num <= 5:
        print(dp[num])
    else:
        dp = [0] * (num+1)
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        dp[5] = 2
        for x in range(6,len(dp)):
            dp[x] = dp[x-2] + dp[x-3]
        
        print(dp[num])
        