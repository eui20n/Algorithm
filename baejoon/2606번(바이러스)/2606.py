# 백준 2606 - 바이러스(bfs)
# 바이러스가 네트워크를 통해 전파가 된다.
# 1번컴퓨터가 바이러스에 감염됬을때, 바이러스에 감염이 되는 컴퓨터의 수를 출력하라
# 입력은 첫줄에 컴퓨터 수(100이하), 두번째 줄에는 네트워크 상에서 직접연결되어 있는 컴퓨터 쌍의 수가 주어진다
# 마지막에는 연결되어 있는 컴퓨터의 번호쌍이 주어진다
# 출력할때 1번 컴퓨터의 경우는 제외하고 감염된 컴퓨터의 수를 출력하면 된다

NUM = int(input()) # 컴퓨터의 수
CON = int(input()) # 직접연결된 쌍의 수

graph = [[] for _ in range(NUM+1)] # 1번부터 시작하는 그래프라서 헷갈리지 않게 하기 위해서 NUM+1로 함
# 원하는 형태의 입력으로 바꾸어 주는 과정
for _ in range(CON):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
visited = [False]*(NUM+1)

from collections import deque

#bsf함수 생성
COM_NUM = []
def bfs(visited,graph,start):
    q = deque([start])
    visited[start] = True
    while q:
        p = q.popleft()
        COM_NUM.append(p)
        for x in graph[p]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
                
bfs(visited,graph,1)
print(len(COM_NUM)-1)
    