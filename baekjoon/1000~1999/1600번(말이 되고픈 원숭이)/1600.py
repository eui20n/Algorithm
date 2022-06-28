"""
    문제 이름 : 말이 되고픈 원숭이
    URL : https://www.acmicpc.net/problem/1600
    ----------------------------------------------
    <문제 설명>
    시작점에서 도착점으로 가는 bfs문제
    지정된 횟수 만큼만 말의 움직임으로 갈 수 있다 -> 말의 움직임은 장애물도 넘을 수 있다
    이 때 도착하는데 걸리는 최소값을 구해라
    갈 수 없으면 -1을 출력해라
"""
from collections import deque

cnt_horse_moving = int(input())
C, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[0] * C for _ in range(cnt_horse_moving + 1)]
    return visited


def go_monkey():
    """ 원숭이가 이동하는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dx_horse = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy_horse = [-2, -1, 1, 2, -2, -1, 1, 2]

    visited = visited_init()
    visited[0][0] |= (1 << 0)

    q = deque()
    # x, y, time, 말 형태 이동 횟수
    q.append([0, 0, 0, 0])

    while q:
        x, y, time, cnt = q.popleft()
        if x == R - 1 and y == C - 1:
            return time

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if board[nx][ny] == 1:
                continue
            if visited[cnt][ny] & (1 << nx):
                continue

            q.append([nx, ny, time + 1, cnt])
            visited[cnt][ny] |= (1 << nx)

        for z in range(8):
            nx = x + dx_horse[z]
            ny = y + dy_horse[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if cnt >= cnt_horse_moving:
                break
            if board[nx][ny] == 1:
                continue
            if visited[cnt + 1][ny] & (1 << nx):
                continue

            q.append([nx, ny, time + 1, cnt + 1])
            visited[cnt + 1][ny] |= (1 << nx)

    return -1


print(go_monkey())


"""
        소요 시간
    1. 30분 조금 덜 걸림
    
        핵심 정리 
    1. 그냥 벽 부수고 이동하기 하위호환 문제
    2. (말의 형태로 이동할 수 있는 경우의 수 -> 입력으로 들어오는 cnt_horse_moving ) + 1 만큼 방문처리 리스트를 3차원으로 만들어 주면 됨
    3. 나는 2차원으로 해서 비트마스킹으로 함
"""