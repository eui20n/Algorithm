# 1로 만들기2
# 정수 X를 아래의 규칙을 사용해서 1로 만들면 된다
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다
# 2. X가 2로 나누어 떨어지면, 2로 나눈다
# 3. 1을 뺀다
# 1을 만들때 사용하는 연산수의 최솟값과 연산을 출력해라

N = int(input())

dp = [[] for _ in range(1000001)]

dp[1].append(1)
dp[2].extend([1,2])
dp[3].extend([1,3])


for x in range(4,len(dp)):
    if x % 2 != 0 and x % 3 != 0:
        dp[x].extend(dp[x-1])
        dp[x].append(x)
    elif x % 3 == 0 and x % 2 ==0:
        if len(dp[x//3]) <= len(dp[x//2]):
            a = x//3
        else:
            a = x//2
        dp[x].extend(dp[a])
        dp[x].append(x)
    elif x % 3 == 0:
        if len(dp[x//3]) <= len(dp[x-1]):
            a = x//3
        else:
            a = x-1
        dp[x].extend(dp[a])
        dp[x].append(x)
    elif x % 2 == 0:
        if len(dp[x//2]) <= len(dp[x-1]):
            a = x//2
        else:
            a = x-1
        dp[x].extend(dp[a])
        dp[x].append(x)

print(len(dp[N])-1)
print(' '.join(map(str,reversed(dp[N]))))
