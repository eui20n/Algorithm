# 숨바꼭질
# 수빈이는 동생과 숨바꼭질을 하고 있다
# 수빈이는 걷거나 순간이동이 가능하다, 만약 X위치에서 걷는다면 X-1 or X+1 위치로 가고, 순간이동한다면 2*X위치로 이동한다
# 수빈이와 동생의 위치가 주어졌을때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 출력해라

# a는 수빈, b는 동생
from collections import deque
a,b = map(int,input().split())

visited = [False for _ in range(100001)]

def bfs(start,end):
    #visited = [False for _ in range(100001)]
    q = deque()
    depth = 0
    visited[start] = True
    q.append([start,depth])
    while q:
        p = q.popleft()
        #print(p)
        if p[0] == end:
            print(p[1])
            break
        
        for z in range(3):
            if z == 0:
                nx = p[0] + 1
            if z == 1:
                nx = p[0] - 1
            if z == 2:
                nx = p[0]*2
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                q.append([nx,p[1]+1])
        

    
bfs(a,b)

                
            
        
        
        
        
    
    
    