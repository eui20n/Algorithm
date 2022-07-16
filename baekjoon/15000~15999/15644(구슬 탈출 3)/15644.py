"""
    문제 이름 : 구슬 탈출 3
    URL : https://www.acmicpc.net/problem/15644
    ----------------------------------------------
    <문제 설명>
    각 공은 동시에 움직이며, 빨간색 구슬만 빼고 싶은 것
    구슬을 탈출하기 위해서 판을 몇번 기울이면 되는지, 또한 어느 방향으로 기울여야 하는지 출력하면 됨
"""
from collections import deque

R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]


def show_arr(arr: list) -> None:
    """ 배열을 출력해주는 함수 """
    print(*arr, sep='\n')


def check_loc_marble() -> tuple:
    """ 빨간색과 파란색 구슬의 초기 위치를 찾아주는 함수 """
    red_marble = []
    blue_marble = []

    for x in range(R):
        for y in range(C):
            if board[x][y] == "R":
                red_marble += [x, y]
                board[x][y] = '.'

            elif board[x][y] == "B":
                blue_marble += [x, y]
                board[x][y] = '.'

    return red_marble, blue_marble


def move_marble(red_x, red_y, blue_x, blue_y) -> str:
    """ 구슬이 움직이는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    d = ["U", "D", "L", "R"]

    q = deque()
    q.append([red_x, red_y, blue_x, blue_y, ""])

    while q:
        red_x, red_y, blue_x, blue_y, go_marble = q.popleft()

        if len(go_marble) >= 10:
            return "-1"

        for z in range(4):
            red_nx, red_ny, blue_nx, blue_ny = red_x, red_y, blue_x, blue_y

            end_game = False
            not_end_game = True
            red_same_blue = False
            blue_same_red = False

            while True:
                red_nx += dx[z]
                red_ny += dy[z]

                if board[red_nx][red_ny] == "#":
                    red_nx -= dx[z]
                    red_ny -= dy[z]
                    break

                if red_nx == blue_x and red_ny == blue_y:
                    red_same_blue = True
                    break

                if board[red_nx][red_ny] == "O":
                    end_game = True
                    break

            while True:
                blue_nx += dx[z]
                blue_ny += dy[z]

                if board[blue_nx][blue_ny] == "#":
                    blue_nx -= dx[z]
                    blue_ny -= dy[z]
                    break

                if board[blue_nx][blue_ny] == "O":
                    not_end_game = False
                    break

                if red_nx == blue_nx and red_ny == blue_ny and not red_same_blue:
                    blue_same_red = True
                    break

            if red_same_blue:
                red_nx = blue_nx - dx[z]
                red_ny = blue_ny - dy[z]

            if blue_same_red:
                blue_nx = red_nx - dx[z]
                blue_ny = red_ny - dy[z]

            if red_nx == red_x and red_ny == red_y and blue_nx == blue_x and blue_ny == blue_y:
                continue

            # print(f"red = {(red_nx, red_ny)}, blue = {(blue_nx, blue_ny)}")

            if not end_game and not_end_game:
                q.append([red_nx, red_ny, blue_nx, blue_ny, go_marble + d[z]])

            elif end_game and not_end_game:
                return go_marble + d[z]

    return "-1"


def main():
    """ 함수를 실행 시켜줄 함수 """
    red_marble, blue_marble = check_loc_marble()
    go_marble = move_marble(red_marble[0], red_marble[1], blue_marble[0], blue_marble[1])
    if go_marble == "-1":
        print(-1)
    else:
        print(len(go_marble))
        print(go_marble)


main()

# 위로 가는 것 -> (-1, 0)
# 아래로 가는 것 -> (1, 0)
# 왼쪽으로 가는 것 -> (0, -1)
# 오른쪽으로 가는 것 -> (0, 1)


"""
        핵심 정리
    1. 빨간 구슬과 파란 구슬이 겹칠 수 있는 경우도 생각해야함
    2. 빨간 구슬과 파란 구슬이 탈출할 수 있는 경우에 대해서 잘 생각해서 코딩하면 됨
"""
