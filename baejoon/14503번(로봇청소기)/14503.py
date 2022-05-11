"""
    문제 이름 : 로봇 청소기
    URL : https://www.acmicpc.net/problem/14503
    ----------------------------------------------
    <문제 설명>
    로봇 청소기가 아래의 규칙에 따라서 작동한다
    1. 현재 위치 청소
    2. 현재 위치에서 다음을 반복하면서 인접한 칸을 탐색
    2-1. 현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면, 왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번함
         그렇지 않을 경우, 왼쪽 방향으로 회전, 이때 방향의 기준은 바라보고 있는 방향임
    2-2. 1번으로 돌아가거나 후진하지 않고 2-1번 단계가 연속으로 네 번 실행되었을 경우, 바로 뒤쪽이 벽이라면 멈춤
         그렇지 않다면 한 칸 후진
         -> 후진을 하면 다시 2-2.번을 해야하는 듯

    방향 -> 0 북쪽, 1 동쪽, 2 남쪽, 3 서쪽
"""
from collections import deque

R, C = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]


def visited_init():
    """ 방문처리 리스트를 만들어 주는 함수, 방문처리의 역할은 청소를 했다는 의미임 """
    visited = [[False] * C for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if graph[x][y] == 1:
                visited[x][y] = True

    return visited


def cleaner(x, y, d):
    """ 청소를 해주는 함수 """
    visited = visited_init()
    visited[x][y] = True

    q = deque()
    q.append([x, y, d])  # 행 위치, 열 위치, 방향 정보

    time = 1

    while q:
        x, y, d = q.popleft()

        dir = dir_search(x, y, d, visited, 0)

        if dir:
            q.append([dir[0], dir[1], dir[2]])
            visited[dir[0]][dir[1]] = True
            time += 1
            continue

        back = back_search(x, y, d, visited)

        if back:
            q.append([back[0], back[1], back[2]])
            visited[back[0]][back[1]] = True
            time += 1
            continue

    return time


def dir_search(x, y, d, visited, cnt):
    """ 방향을 탐색해주는 함수 """
    if cnt == 4:
        return False

    if d == 0:
        if visited[x][y - 1]:
            result = dir_search(x, y, 3, visited, cnt + 1)

        else:
            result = [x, y - 1, 3]
            return result

    elif d == 1:
        if visited[x - 1][y]:
            result = dir_search(x, y, 0, visited, cnt + 1)

        else:
            result = [x - 1, y, 0]
            return result

    elif d == 2:
        if visited[x][y + 1]:
            result = dir_search(x, y, 1, visited, cnt + 1)

        else:
            result = [x, y + 1, 1]
            return result

    elif d == 3:
        if visited[x + 1][y]:
            result = dir_search(x, y, 2, visited, cnt + 1)

        else:
            result = [x + 1, y, 2]
            return result

    return result


def back_search(x, y, d, visited):
    """ 후진해주는 함수 """
    if d == 0:
        if graph[x + 1][y] == 1:
            return False

        elif not dir_search(x + 1, y, d, visited, 0):
            return back_search(x + 1, y, d, visited)

        else:
            return dir_search(x + 1, y, d, visited, 0)

    elif d == 1:
        if graph[x][y - 1] == 1:
            return False

        elif not dir_search(x, y - 1, d, visited, 0):
            return back_search(x, y - 1, d, visited)

        else:
            return dir_search(x, y - 1, d, visited, 0)

    elif d == 2:
        if graph[x - 1][y] == 1:
            return False

        elif not dir_search(x - 1, y, d, visited, 0):
            return back_search(x - 1, y, d, visited)

        else:
            return dir_search(x - 1, y, d, visited, 0)

    elif d == 3:
        if graph[x][y + 1] == 1:
            return False

        elif not dir_search(x, y + 1, d, visited, 0):
            return back_search(x, y + 1, d, visited)

        else:
            return dir_search(x, y + 1, d, visited, 0)


print(cleaner(x, y, d))
