"""
    문제 이름 : 다리 만들기
    URL : https://www.acmicpc.net/problem/2146
    ----------------------------------------------
    <문제 설명>
    가장 짧게 만들 수 있는 다리의 길이가 몇인지 출력하면 됨
"""
from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [0] * N
    return visited


def land_sea(visited):
    """ 섬 외엔 모두 True로 바꿔주는 함수 """
    for x in range(N):
        for y in range(N):
            if graph[x][y] == 0:
                visited[y] |= 1 << x

    return visited


def sep_land_bfs(x, y, visited, cnt):
    """ 섬을 구분하기 위해서 bfs를 돌려주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[y] |= 1 << x
    graph[x][y] = cnt

    q = deque()
    q.append([x, y])

    while q:
        p = q.popleft()
        for z in range(4):
            nx = p[0] + dx[z]
            ny = p[1] + dy[z]
            if sep_land_con(nx, ny, visited):
                graph[nx][ny] = cnt
                visited[ny] |= 1 << nx
                q.append([nx, ny])


def sep_land_con(x, y, visited):
    """ 섬을 구분해주는 조건 """
    if 0 > x or x >= N:
        return False
    if 0 > y or y >= N:
        return False
    if visited[y] & 1 << x:
        return False
    return True


def sep_land():
    """ 섬을 구분해 주고 시작점을 반환해주는 함수 """
    visited = visited_init()
    visited = land_sea(visited)

    start_point = []

    cnt = 1
    for x in range(N):
        for y in range(N):
            if not (visited[y] & 1 << x):
                sep_land_bfs(x, y, visited, cnt)
                start_point.append([x, y])
                cnt += 1

    return start_point


def make_brige(x, y):
    """ 다리를 만들어 주는 함수 """

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = visited_init()
    visited[y] |= 1 << x

    temp = [[float('inf')] * N for _ in range(N)]

    q = deque()
    q.append([x, y, 0, graph[x][y], graph[x][y]])  # x, y, 거리, 출발한 위치, 현재 위치
    result = float('inf')

    while q:
        x, y, distance, start_loc, pre_loc = q.popleft()

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if make_brige_con(nx, ny, visited, temp, distance):
                if result <= distance:
                    continue

                # 아직 육지일때
                if start_loc == graph[nx][ny]:
                    q.append([nx, ny, distance, start_loc, pre_loc])
                    visited[ny] |= 1 << nx

                # 바다일때
                elif graph[nx][ny] == 0:
                    q.append([nx, ny, distance + 1, start_loc, graph[nx][ny]])
                    temp[nx][ny] = distance + 1

                # 바다에서 출발한 육지를 밟았을때
                elif graph[nx][ny] == start_loc and pre_loc == 0:
                    continue

                # 다른 육지를 밟았을때
                elif graph[nx][ny] != 0 and graph[nx][ny] != start_loc:
                    if result > distance:
                        result = distance

    return result


def make_brige_con(x, y, visited, temp, distance):
    """ make_brige_con 조건 """
    if 0 > x or x >= N:
        return False
    if 0 > y or y >= N:
        return False
    if visited[y] & 1 << x:
        return False
    if temp[x][y] <= distance + 1:
        return False
    return True


def main():
    """ 함수를 실행시켜 주는 함수 """
    start_point = sep_land()
    result = float('inf')
    for x in start_point:
        cnt = make_brige(x[0], x[1])
        if cnt < result:
            result = cnt

    return result


print(main())

"""
    핵심 정리
    큐에 쓸데 없는 것이 들어가면 안됨
    이것만 신경쓰면 쉽게 해결이 가능한데, 이걸 해결 못하면 힘듬
    본인은 힘들었음
"""
