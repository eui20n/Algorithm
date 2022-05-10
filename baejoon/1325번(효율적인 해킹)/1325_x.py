# 효율적인 해킹
# 그래프가 주어졌을때 깊이가 가장 깊은거를 출력하면 됨

from collections import deque
import sys

N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
start = []

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    start.append(b)
    graph[b].append(a)

start = list(set(start))

def dfs(start):
    # count = 0 이 왜 안될까
    if visited[start] == True:
        return
    visited[start] = True
    for x in graph[start]:
        dfs(x)
    count[0] +=1
    return count[0]

num = 0
result = []
for x in start:
    count = [0]
    visited = [False for _ in range(N+1)]
    k = dfs(x)
    if num > k:
        pass
    elif num <= k:
        num = k
        result.append(x)
print(' '.join(map(str,result)))

# bfs로 하기