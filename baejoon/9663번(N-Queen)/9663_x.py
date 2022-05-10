# N-Queen
# N x N 인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
# N이 주어졌을때, 퀸을 놓는 방법의 수를 구하여라

N = int(input())
Queen = [0] * N
result = 0

def check_queen(x): # x는 현재 위치
    for z in range(x):
        if Queen[x] == Queen[z] or abs(Queen[x]-Queen[z]) == x - z:
            return False
    return True

def dfs(n):
    global result
    if n == N:
        result +=1
    else:
        for i in range(N):
            Queen[n] = i
            if check_queen(n):
                dfs(n+1)
dfs(0)
print(result)
    
# 풀이 봄... 다음에 다시 풀어보기