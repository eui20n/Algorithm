"""
    문제 이름 : 수영장 만들기
    URL : https://www.acmicpc.net/problem/1113
    ----------------------------------------------
    <문제 설명>
    그래프가 주어질때 물이 고일 수 있는지, 그리고 고인다면 얼마나 고이는지 출력하면 된다.
    1 <= 물의 높이 <= 9 이다
    무조건 물이 고일 수 있다고 생각할 것 -> 물이 고일 수 없을시 출력값이 없음
"""
from collections import deque

R, C = map(int, input().split())
graph = [list(map(int, input())) for _ in range(R)]
area = [[False] * C for _ in range(R)]


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False] * C for _ in range(R)]
    return visited


def area_find():
    """ 구역을 나눠주는 함수 """

    cnt = 0
    for x in range(R):
        for y in range(C):
            if not area[x][y]:
                cnt += 1
                sep_area(x, y, cnt)


def sep_area(x, y, cnt):
    """ 구역을 한 번 나누는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = visited_init()

    visited[x][y] = True
    area[x][y] = cnt

    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if con_sep_area(nx, ny, x, y, visited):
                q.append([nx, ny])
                area[nx][ny] = cnt
                visited[nx][ny] = True


def con_sep_area(nx, ny, x, y, visited):
    if 0 > nx or nx >= R:
        return False
    if 0 > ny or ny >= C:
        return False
    if visited[nx][ny]:
        return False
    if graph[x][y] != graph[nx][ny]:
        return False
    return True


area_find()
print(*area, sep='\n')

# 임시 리스트를 만들고 임시 리스트에서 변경 값을 저장함, 그 후 원래 리스트와 임시 리스트의 차이를 구해서 더하면 됨
# 이어져 있는지 확인하면 됨 -> 현재 기준에서 위와 아래로 같은지, 양 옆으로 같은지 확인하면 됨
# 영역을 먼저 구하는게 맞을 듯
