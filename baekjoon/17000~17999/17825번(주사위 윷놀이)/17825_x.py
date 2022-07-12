"""
    문제 이름 : 주사위 윷놀이
    URL : https://www.acmicpc.net/problem/17825
    ----------------------------------------------
    <문제 설명>
    처음에는 시작칸에 4개의 말이 있다. 말은 판에 그려진 화살표 방향대로만 이동할 수 있다
    말이 파란색 칸에서 시작하면 파란색 화살표로 가야한다 => 이동하는 도중에 파란색 칸으로 가면 그 때는 파란색 화살표가 아닌 빨간색 화살표
    게임은 10개의 턴으로 이루어진다. 매 턴마다 1부터 5까지 한 면에 하나씩 적혀있는 5면체 주사위를 굴리고
    도착 칸에 있지 않은 말을 하나 골라 주사위에 나온 수만큼 이동시킨다
    만약 이동해야 하는 칸에 말이 있다면, 그 칸으로 이동할 수 없다 -> 도착 칸은 가능
    말이 이동을 마칠 때 마다 칸에 적혀 있는 수가 점수에 추가가 된다

    주사위에서 나올 수 10개를 미리 알고 있을 때, 얻을 수 있는 점수의 최댓값을 구해보자

"""
from copy import deepcopy

N = list(map(int, input().split()))
board = [[0] * 21 for _ in range(5)]
dir_board = [[0] * 21 for _ in range(5)]
visited = [[0] * 21 for _ in range(5)]


def change_board():
    """ 보드를 만드는 함수로, 내가 만든 기준에 맞게 숫자를 넣어줄 것 """
    red_area = [-1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
    blue_5 = [10, 13, 16, 19]
    blue_10 = [20, 22, 24]
    blue_15 = [30, 28, 27, 26]
    blue_25 = [40, 35, 30, 25]

    for y in range(21):
        board[0][y] = red_area[y]

    for x in range(4):
        board[x][5] = blue_5[x]
        board[x][15] = blue_15[x]
        board[x][20] = blue_25[x]

    for x in range(3):
        board[x][10] = blue_10[x]

    board[1][0] = -2


def change_dir_board():
    """ dir_board를 알맞는 방향을 바꿔주는 함수 """
    for y in range(21):
        dir_board[0][y] = [1]

    for x in range(1, 4):
        dir_board[x][5] = [3]
        dir_board[x][15] = [3]

    for x in range(1, 3):
        dir_board[x][10] = [3]

    dir_board[0][5].append(3)
    dir_board[0][10].append(3)
    dir_board[0][15].append(3)

    dir_board[4][5] = [-1, 3, 20]
    dir_board[4][15] = [-1, 3, 20]
    dir_board[3][10] = [-1, 3, 20]

    dir_board[3][20] = [4]
    dir_board[2][20] = [4]
    dir_board[1][20] = [4]

    dir_board[1][0] = [-1]


def dice_yut_game():
    """ 주사위 윷놀이를 하는 함수 """
    pass


# piece는 현재위치가 튜플로 담겨 있음
def go_piece(piece, num):
    """ 말이 앞으로 가는 함수 """
    dx = [0, 0, 0, 1, -1]
    dy = [0, 1, -1, 0, 0]

    x = piece[0]
    y = piece[1]
    arrive = False

    # 현재위치의 방향이 2개라는 것은 그 위치는 파란 색칸임
    if len(dir_board[x][y]) == 2:
        d = dir_board[x][y][1]

    elif len(dir_board[x][y]) == 1:
        d = dir_board[x][y][0]

    while True:
        if num == 0:
            break

        x = x + dx[d]
        y = y + dy[d]
        d = dir_board[x][y][0]
        num -= 1

        if len(dir_board[x][y]) == 3:
            x = dir_board[x][y][1]
            y = dir_board[x][y][2]
            d = 4

        # 도착점에 도착함
        if 0 > x or x >= 21:
            arrive = True
            break
        if 0 > y or y >= 5:
            arrive = True
            break

    if arrive:
        pass

    if not visited[x][y]:
        visited[x][y] = True
        visited[piece[0]][piece[1]] = False
        piece[0] = x
        piece[1] = y


change_board()
change_dir_board()
print(*dir_board, sep='\n')
print()
print(*board, sep='\n')
