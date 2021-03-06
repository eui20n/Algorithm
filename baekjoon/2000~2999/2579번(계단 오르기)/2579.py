# 계단 오르기
# 각 계단에 점수가 있다
# 계단을 오르는 규칙은 아래와 같다
# 1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다
# 2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다
# 3. 마지막 도착 계단은 반드시 밟아야 한다
# 위 규칙으로 계단을 오를때, 얻을 수 있는 점수의 최대값을 출력해라
# 입력은 계단의 수와 계단의 점수이다
# 출력은 점수의 최대값이다

N = int(input())
step = []
for _ in range(N):
    a = int(input())
    step.append(a)
    

dp = [0] * (N+1)
dp[1] = step[0]
#dp[2] = dp[1] + step[1]
count = 0 # 연속으로 2개의 칸을 오르지 못하기 때문에 count로 몇개의 칸을 갔는지 세어줌

for x in range(2,N+1):
    if count == 1: # 한칸 이동했을때 -> 다음칸으로 가면 총 3개의 계단을 연속으로 이동한 것이 됨 
        dp[x] = max(dp[x-2] + step[x-1],dp[x-3] + step[x-2] + step[x-1]) # 앞의 식 -> 전전의 계단(그 때의 dp값 -> 최대값)에서 바로 온 경우, 뒤의 식 -> 전전전의 계단에서 전 계단, 그리고 현재 계단으로 온 경우
        # 신경써야할것은 dp의 값이 최대값이지만, 조건에 의해서 만들어진 최대값임. 즉, 각각의 계단의 최대값은 연속된 3개의 계단을 오르지 못하는 규칙에 의해서 만들어진 값임
        # --> 그럼 현재의 계단에서의 최대값은 그 계단에서의 바로 구해진 최대값이 아니라 전전이나 전전전에서 구해진 최대값을 사용해서 구해야됨
        if dp[x] == dp[x-3] + step[x-2] + step[x-1]:
            count = 1 # 바로 전 계단에서 온 경우 count를 해줌
        else:
            count = 0 # 바로 전 계단에서 온 경우가 아니면 count를 안해줌
    else:
        dp[x] = max(dp[x-1],dp[x-2])+step[x-1]
        if dp[x] == dp[x-1] + step[x-1]:
            count +=1
        else:
            count = 0
    
          
print(dp[N]) # 원하는 곳의 최대값 출력
