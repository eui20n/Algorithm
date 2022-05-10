# 1,2,3 더하기
# 테스트 케이스가 입력이 되고
# 다음줄에 정수가 입력이 됨
# 이 정수를 1,2,3으로 만들때 몇번이 필요한지 출력해라

T = int(input())
for i in range(T):
    n = int(input())
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for x in range(4,len(dp)):
        dp[x] = dp[x-1] + dp[x-2] + dp[x-3]
        
    print(dp[n])
    