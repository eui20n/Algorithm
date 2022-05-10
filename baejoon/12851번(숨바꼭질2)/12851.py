# 숨박꼭질2
# 숨박꼭질과 같지만, 가장 빨리 찾는 경우와 그 경우가 몇개인지 출력하는 문제
# 이동은 매초 x-1, x+1, 2x

from collections import deque
a,b = map(int,input().split())

# 걸린 시간과 그때의 경우의 수
visited = [[float('inf'),0] for _ in range(100001)]

def bfs(a,b):
    q = deque()
    q.append([a,0])
    
    visited[a][0] = 0
    visited[a][1] = 1
    
    while q:
        p = q.popleft()
        if p[0] == b:
            return p[1]
        for z in [-1,1,p[0]]:
            np = p[0] + z
            if 0 <= np <= 100000 and visited[np][0] >= p[1]:
                visited[np][0] = p[1]
                q.append([np,p[1]+1])
                visited[np][1] +=1

print(bfs(a,b),visited[b][1],sep = '\n')
