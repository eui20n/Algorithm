# 병사 배치하기
# 병사가 랜덤하게 배치가 되어 있다
# 그 병사들은 각각 전투력을 가지고 있다
# 자기 뒤에 있는 병사는 앞에 있는 병사보다 전투력이 낮아야 한다
# 위의 규칙에 따라서 병사를 열외 시켜야 하는데, 이때 남아있는 병사의 수가 최대가 되게 하고 싶을때
# 열외해야 하는 병사의 수를 출력해라

N = int(input())
num = list(map(int,input().split()))
num.reverse()

dp = [1] * (N+1)
for x in range(1,len(dp)):
    for y in range(x,0,-1):
        if num[x-1] <= num[y-1]:
            pass
        else:
            dp[x] = max(dp[x],dp[y]+1)
            
print(N-max(dp))

# 가장 긴 증가하는 부분수열과 같은 문제