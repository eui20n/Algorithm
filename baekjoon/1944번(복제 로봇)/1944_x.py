"""
    문제 이름 : 복제 로봇
    URL : https://www.acmicpc.net/problem/1944
    ----------------------------------------------
    <문제 설명>
    복제 로봇이 미로로 감 -> 입구와 열쇠가 있는 곳에 로봇을 복제함
    --> 모든 열쇠를 찾으면서 로봇이 움직이는 횟수의 합을 최소로 하는 프로그램을 만들어라
    --> 만약에 열쇠를 다 먹을 수 없으면 -1 출력
"""
from collections import deque

N, cnt_key = map(int, input().split())
miro = [list(map(str, input())) for _ in range(N)]


def loc_robot():
    """ 초기의 시작점을 찾아주는 함수 """
    for x in range(N):
        for y in range(N):
            if miro[x][y] == 'S':
                return x, y


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False] * N for _ in range(N)]
    return visited


def check_dist(x, y):
    """ 거리를 확인하는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = visited_init()
    visited[x][y] = True

    q = deque()
    q.append([x, y, 0, (x, y)])  # x좌표, y좌료, 길이, 처음이 뭔지 -> 그게 뭔지 보면 열쇠가 구분이 안되서 좌표로 가져갈 것

    node_node_list = []  # 가중치, 노드, 노드를 담아줄 리스트 -> 정수, 튜플, 튜플

    while q:
        x, y, dist, check = q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            if miro[nx][ny] == '1':
                continue

            if miro[nx][ny] == 'K':
                if check[0] == nx and check[1] == ny:
                    continue

                node_node_list.append([dist + 1, (nx, ny), check])
                q.append([nx, ny, dist + 1, (nx, ny)])
                visited = visited_init()
                visited[nx][ny] = True
                continue

            q.append([nx, ny, dist + 1, check])
            visited[nx][ny] = True

    return node_node_list


x, y = loc_robot()
print(check_dist(x, y))

# 시작점 - K
# 다른 K - 다른 K
# 방문 처리 고민하기