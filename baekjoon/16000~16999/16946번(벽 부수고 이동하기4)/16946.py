"""
    문제 이름 : 벽 부수고 이동하기4
    URL : https://www.acmicpc.net/problem/16946
    ----------------------------------------------
    <문제 설명>
    0은 이동 가능한 칸, 1은 벽이다.
    각각의 벽에 대해서 아래를 구하면 된다.
    1. 벽을 부수고 이동할 수 있는 곳으로 변경한다.
    2. 그 위치에서 이동할 수 있는 칸의 개수를 세어보면 된다.
"""
from collections import deque

R, C = map(int, input().split())
board = [list(map(int, input())) for _ in range(R)]
board_0 = [[0] * C for _ in range(R)]
board_sep = [[0] * C for _ in range(R)]


def show_arr(arr):
    """ 배열을 보여주는 함수 """
    print(*arr, sep='\n')
    print()


def visited_init():
    """ 방문처리 리스트를 만들어 주는 함수 """
    visited = [[False] * C for _ in range(R)]
    return visited


def num_move(x, y, visited):
    """ 이동 가능한 칸은 얼마나 이동가능한지 구해주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = True

    q = deque()
    q.append([x, y])

    temp = [[x, y]]
    cnt = 1

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
                continue

            temp.append([nx, ny])
            q.append([nx, ny])
            visited[nx][ny] = True
            cnt += 1

    return temp, cnt


def change_board_0_sep(arr, num, cnt):
    """ board_0와 board_sep를 바꿔줄 함수 """
    for x, y in arr:
        board_0[x][y] = num
        board_sep[x][y] = cnt


def change_board(x, y):
    """ board를 바꿔줄 함수 -> 벽을 하나 지웠을 때 움직일 수 있는 거리로 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    unique_sep = set()

    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 > nx or nx >= R:
            continue
        if 0 > ny or ny >= C:
            continue
        if board[nx][ny]:
            continue
        if board_sep[nx][ny] in unique_sep:
            continue

        board[x][y] += board_0[nx][ny]
        unique_sep.add(board_sep[nx][ny])

    board[x][y] = board[x][y] % 10


def main():
    """ 함수를 실행 시켜줄 함수 """
    visited = visited_init()
    cnt = 1
    for x in range(R):
        for y in range(C):
            if not visited[x][y] and board[x][y] == 0:
                move_list, num = num_move(x, y, visited)
                change_board_0_sep(move_list, num, cnt)
                cnt += 1

    for x in range(R):
        for y in range(C):
            if board[x][y] == 1:
                change_board(x, y)


def print_result():
    """ 정답을 출력해주는 함수 """
    main()
    for x in board:
        print("".join(map(str, x)))


print_result()


"""
        핵심 정리
    1. 벽을 부수기 전에, 원래 갈수 있는 칸이 얼마나 갈 수 있는지 확인해야함
    => dfs쓰던 bfs쓰던 확인하면 되는데, bfs로 확인하는게 더 편했음
    2. 확인했으면 0인 부분을 얼마나 갈 수 있는지 새로운 수를 대입해줌
    3. 1인 부분에서 4방향을 보고, 0이 였던 부분은 더해주면 되는데, 중복으로 더해지는 경우가 생김
    3-1. 중복으로 더해지는 부분만 구분해주면 됨
"""