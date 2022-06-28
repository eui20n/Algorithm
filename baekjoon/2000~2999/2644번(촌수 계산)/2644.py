# 촌수계산
# 촌수 계산하면 되는 문제
# 사람들은 1,2,3,...,n 의 연속도니 번호가 표시됨, 첫번째 줄에는 전체 사람의 수 n이 주어짐
# 두번째 줄에는 촌수를 촌수를 계산해야 하는 서로 다른 사람의 번호가 주어짐
# 세번째 줄에는 부모 자식들 간의 관계의 개수 m이 주어짐
# 네번째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각각 나옴
# 출력은 요구하는 두 사람의 촌수를 정수로 출력, 만약에 촌수 계산을 할 수 없으면 -1 출력

from collections import deque

N = int(input())
a,b = map(int,input().split())
m = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
visited = [False] * (N+1)

def bfs(start,end):
    visited[start] = True
    depth = 1
    q = deque()
    q.append([graph[start],depth])
    p = []
    while q:
        p = q.popleft()
        if end in p[0]:
            break
        for x in p[0]:
            if not visited[x]:
                visited[x] = True
                q.append([graph[x],p[1]+1])
    if end in p[0]:
        print(p[1])
    else:
        print(-1)

bfs(a,b)
    
    
    
    
    