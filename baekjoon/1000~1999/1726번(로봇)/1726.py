"""
    문제 이름 : 로봇
    URL : https://www.acmicpc.net/problem/1726
    ----------------------------------------------
    <문제 설명>
    로봇을 이동을 제어하는 명령
    1. Go k: k는 1, 2 또는 3 일 수 있고, 현재 향하고 있는 방향으로 k칸 만큼 움직인다.
    2. Turn dir: dir은 left또는 right이며, 각각 왼쪽 또는 오른쪽으로 90도 회전한다
    0 -> 로봇이 갈 수 있는 길
    1 -> 로봇이 못 가는 길

    로봇의 위치와 방향이 주어졌을 때, 원하는 위치로 가고, 방향을 바라보도록 하는 최소 명령의 수를 구해라
    동 -> 1(0,1), 서 -> 2(0,-1), 남 -> 3(1,0), 북 -> 4(-1,0)
"""
from collections import deque

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

robot_loc_dir = []
a, b, c = map(int, input().split())
robot_loc_dir.extend([a - 1, b - 1, c])

robot_go_loc_dir = []
a, b, c = map(int, input().split())
robot_go_loc_dir.extend([a - 1, b - 1, c])


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False] * C for _ in range(R)]
    return visited


def go_robot(start, end):
    """ 로봇이 움직이는 함수 """
    direction = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

    visited = visited_init()
    visited[start[0]][start[1]] = True

    q = deque()
    q.append([start[0], start[1], start[2], 0, 0])

    while q:
        x, y, robot_dir, time, cnt = q.popleft()

        if x == end[0] and y == end[1] and robot_dir == end[2]:
            return time

        for go in [1, 2, 3]:
            nx = x + direction[robot_dir][0] * go
            ny = y + direction[robot_dir][1] * go
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 1:
                break

            q.append([nx, ny, robot_dir, time + 1, 0])
            visited[nx][ny] = True

        if cnt < 4:
            if robot_dir == 1 or robot_dir == 2:
                q.append([x, y, 3, time + 1, cnt + 1])
                q.append([x, y, 4, time + 1, cnt + 1])

            elif robot_dir == 3 or robot_dir == 4:
                q.append([x, y, 1, time + 1, cnt + 1])
                q.append([x, y, 2, time + 1, cnt + 1])


print(go_robot(robot_loc_dir, robot_go_loc_dir))


"""
        핵심정리
    1. 제자리 처리하는게 핵심인거 같음 -> 카운트를 세서 다시 자기 방향이 나오면 멈추는 걸로 했음, 나는 4로 했는데, 2로 해도 충분할 듯
    2. 앞에 로봇이 못 칸이 있는데 더 넘어서 가는 경우만 잘 생각하면 됨
    3. 위의 2가지만 유의해서 풀면 쉽게 풀이 가능
    4. 그리고 제자리를 잘못 구현하면 메모리 초과가 날 것 같음
"""