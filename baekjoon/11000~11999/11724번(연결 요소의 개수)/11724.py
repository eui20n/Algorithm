# 연결 요소의 개수
# 방향이 없는 무향 그래프가 주어졌을때 연결 요소의 개수를 구하여라
from collections import deque

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False for _ in range(N+1)]
def bfs(start):
    q = deque()
    q.append(graph[start])
    visited[start] = True
    while q:
        p = q.popleft()
        for z in p:
            if not visited[z]:
                visited[z] = True
                q.append(graph[z])
                
count = 0
for x in range(1,N+1):
    if visited[x] == False:
        bfs(x)
        count +=1
print(count)
    
# 한번 방문한 곳은 True로 바뀌니 이걸 이용해서 반복문을 사용
    
    
    