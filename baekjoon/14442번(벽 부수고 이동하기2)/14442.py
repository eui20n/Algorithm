"""
    문제 이름 : 벽 부수고 이동하기2
    URL : https://www.acmicpc.net/problem/14442
    ----------------------------------------------
    <문제 설명>
    벽을 K개 까지 부술 수 있을 때, 시작점에서 도착점 까지 가는데 걸리는 최단거리를 구해라
    => 그냥 K개 만큼 리스트를 더 만들어서 풀면 될듯(3차원으로)
"""
from collections import deque

N, M, K = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]


def visited_init():
    """ 방문처리 리스트를 만들어 주는 함수 """
    visited = [[0] * M for _ in range(N)]
    return visited


def break_wall_go():
    """ 벽 부수고 이동하기 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = visited_init()
    visited[0][0] |= (1 << 0)

    q = deque()
    # x, y, time, 부순 벽의 수
    q.append([0, 0, 0, 0])

    while q:
        x, y, time, cnt_wall = q.popleft()
        if x == N - 1 and y == M - 1:
            return time + 1

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= N:
                continue
            if 0 > ny or ny >= M:
                continue

            if graph[nx][ny] == 1 and cnt_wall < K and not visited[nx][ny] & (1 << cnt_wall + 1):
                visited[nx][ny] |= (1 << cnt_wall + 1)
                q.append([nx, ny, time + 1, cnt_wall + 1])

            if graph[nx][ny] == 0 and not visited[nx][ny] & (1 << cnt_wall):
                visited[nx][ny] |= (1 << cnt_wall)
                q.append([nx, ny, time + 1, cnt_wall])

    return -1


print(break_wall_go())


"""
        소요 시간
    약 2시간 정도 걸린 문제
    
        핵심 정리
    1. 개인적으로 정말 레전드 문제 -> 파이썬으로 해결 못할 것 같음
    2. 시간이 엄청나게 많이 빡빡한 문제
    3. 비트마스킹을 활용해서 시간을 최대한 단축시킴
    4. 방문처리를 볼때 다음에 갈 곳도 봐야함 -> 이렇게 안하면 그 곳으로 계속 가기 때문
"""