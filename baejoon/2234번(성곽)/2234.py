# 성곽
# 성곽이 있는데 굵은 선은 벽이고, 점선은 통로이다
# 위와 같은 지도를 입력받아 아래있는 것을 출력하려고 한다
# 1. 이 성에 있는 방의 개수
# 2. 가장 넓은 방의 넓이
# 3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
# 벽의 정보가 비트로 주어짐 -> 서쪽 1, 북쪽 2, 동쪽 4, 남쪽 8 각각의 값을 더해주면 됨

from collections import deque
M,N = map(int,input().split())
info_wall = [list(map(int,input().split())) for _ in range(N)]

graph = [[0]*M for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 비트 마스킹으로 하려고 이렇게 함
visited = [0] * M


def bfs(x,y,k):
    '''가장 넓은 방이랑 방의 개수를 구해주는 함수'''
    visited[y] |= 1 << x
    graph[x][y] = k
    q = deque()
    q.append([x,y])
    cnt = 1
    while q:
        p = q.popleft()
        if 0 <= p[0] -1 < N and 0 <= p[1] < M and not visited[p[1]] & (1 << p[0]-1) and not info_wall[p[0]][p[1]] & 1 << 1: # 북
            q.append([p[0]-1,p[1]])
            visited[p[1]] |= 1 << p[0]-1
            cnt +=1
            graph[p[0]-1][p[1]] = k
            
        if 0 <= p[0] +1 < N and 0 <= p[1] < M and not visited[p[1]] & (1 << p[0]+1) and not info_wall[p[0]][p[1]] & 1 << 3: # 남
            q.append([p[0]+1,p[1]])
            visited[p[1]] |= 1 << p[0]+1
            cnt +=1
            graph[p[0]+1][p[1]] = k
            
        if 0 <= p[0] < N and 0 <= p[1] -1 < M and not visited[p[1]-1] & (1 << p[0]) and not info_wall[p[0]][p[1]] & 1 << 0: # 서
            q.append([p[0],p[1]-1])
            visited[p[1]-1] |= 1 << p[0]
            cnt +=1
            graph[p[0]][p[1]-1] = k
            
        if 0 <= p[0] < N and 0 <= p[1]+1 < M and not visited[p[1]+1] & (1 << p[0]) and not info_wall[p[0]][p[1]] & 1 << 2: # 동
            q.append([p[0],p[1]+1])
            visited[p[1]+1] |= 1 << p[0]
            cnt +=1
            graph[p[0]][p[1]+1] = k
    return cnt

def div_room(count_room,dic_room):
    '''어떤 방들이 연결되어 있는지 확인해 주는 함수'''
    list_room = [[] for _ in range(count_room+1)]
    max_num = []
    for x in range(N):
        for y in range(M):
            for z in range(4):
                nx = x + dx[z]
                ny = y + dy[z]
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] not in list_room[graph[x][y]] and graph[nx][ny] != graph[x][y]:
                    list_room[graph[x][y]].append(graph[nx][ny])
                    max_num.append(dic_room[graph[x][y]] + dic_room[graph[nx][ny]])
    return max(max_num)

def main():
    count_room = 0
    max_count = 0
    dic_room = {}
    for x in range(N):
        for y in range(M):
            if not(visited[y] & 1 << x):
                count_room +=1
                cnt = bfs(x,y,count_room)
                if max_count < cnt:
                    max_count = cnt
            dic_room[count_room] = cnt
    return [count_room,max_count,div_room(count_room,dic_room)]

for x in main():
    print(x)
          
# 이 문제는 곧 죽어도 비트로 생각해서 풀것
# 벽이 없어지는 연산도 비트 마스킹으로 하기
# 벽을 하나 제거했을때 최대 넓이만 구하면 됨
# 문제 다 풀면 check_wall이라고 함수 있는데 추가해서 간단하게 풀어보기 - 노션에 있음