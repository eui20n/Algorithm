# 스타트링크
# 강호가 면접에 늦었다 이런저런;;
# 건물은 총 F층이고 면접 장소는 G층이다, 또한 강호는 현재 S 층에 있고 엘리베이터를 통해 G층으로 가려고 한다
# 이 엘리베이터는 특이하게 위로 가는 U 버튼과 아래로 가는 D버튼 밖에 없다(만약에 위나 아래로 갈 층이 없으면 움직이지 않음)
# 강호가 G층에 도착하려면 버튼을 몇번 눌러야 하는지 출력해라
# 여기서 엘리베이터로 G층에 도달 할 수 없는 경우에는 use the stairs를 출력해라
from collections import deque

F, S, G, U, D = map(int,input().split())

visited = [False for _ in range(F)]

def bfs(F,S,G,U,D):
    q = deque()
    visited[S-1] = True
    depth = 0
    q.append([S-1, depth])
    while q:
        p = q.popleft()
        if p[0] == G-1:
            print(p[1])
            break
        for z in [U,-D]:
            nx = p[0] + z
            if 0 <= nx < F and not visited[nx]:
                visited[nx] = True
                q.append([nx,p[1] + 1])
                
    if visited[G-1] == False:
        print("use the stairs")
                
                
bfs(F,S,G,U,D)
        
        
        
        
        
    
    
    
    
    
    