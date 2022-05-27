# 가장 긴 증가하는 부분 수열
# 증가하는 수열중 가장 긴 수열의 길이를 찾으면 됨

N = int(input())
num = list(map(int,input().split()))


dp = [1] *(N+1)

for x in range(1,len(dp)):
    for y in range(x,0,-1): # 0까지인 이유는 dp테이블을 1부터 시작하는 걸로 만들었기 때문
        if num[y-1] >= num[x-1]:
            pass
        else:
            dp[x] = max(dp[x],dp[y]+1)
        
print(max(dp))

# 본인 위치에 있는 것과 그 뒤에 있는 것들(전부)을 비교함
