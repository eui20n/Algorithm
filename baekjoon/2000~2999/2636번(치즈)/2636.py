"""
    문제 이름 : 치즈
    URL : https://www.acmicpc.net/problem/2636
    ----------------------------------------------
    <문제 설명>
    밖과 닿는 부분의 치즈만 녹음
    이 때, 치즈가 다 녹는데 걸리는 시간을 구해라
"""
from collections import deque


def check_cheese():
    """ 치즈의 영역이 얼마나 있는지 구해주는 함수 """
    result = 0

    for x in range(R):
        for y in range(C):
            if board[x][y] == 1:
                result += 1
    return result


def bfs():
    """ bfs를 해주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[0][0] = True

    q = deque()
    q.append([0, 0])

    melting = []

    while q:
        x, y = q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 1:
                melting.append([nx, ny])
                continue

            q.append([nx, ny])
            visited[nx][ny] = True

    return melting


def melting(arr, cnt):
    """ 녹여주는 함수 """
    for x, y in arr:
        if board[x][y] == 1:
            board[x][y] = 0
            cnt -= 1

    return cnt

def main():
    """ 함수를 실행시켜주는 함수 """
    cnt_cheese = check_cheese()
    time = 0
    temp_cheese = 0

    while True:
        if cnt_cheese == 0:
            break

        melting_cheese = bfs()
        temp_cheese = cnt_cheese
        cnt_cheese = melting(melting_cheese, cnt_cheese)

        time += 1

    print(time, temp_cheese, sep="\n")


if __name__ == "__main__":
    R, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    main()


"""
        소요 시간
    10분
    
        핵심 정리
    1. 시작을 가장에서 하면 됨 => 가장 자리에는 무조건 치즈가 없음
    2. 완전 탐색해도됨 => 가로 세로 최대값이 100이라서 시간 충분함
    2-1. 만약에 완전 탐색하면 안되면, 녹은 치즈의 좌표를 저장해서 거기서 bfs돌리면 됨
"""