"""
    문제 이름 : 새로운 게임2
    URL : https://www.acmicpc.net/problem/17837
    ----------------------------------------------
    <문제 설명>
    A번 말이 이동하려는 칸이 흰색인 경우
    - 그 칸으로 이동한다. 근데 그 칸에 이미 다른 말이 있으면 A번 말을 가장 위에 놓는다
    - 만약 A번 말 위에 다른 말이 있으면 A번 말과 위에 있는 모든 말이 이동한다
    ==> 위 아래 개념이 있음
    A번 말이 이동하려는 칸이 빨간색인 경우
    - A번 말과 그 위에 있는 모든 말의 쌓여 있는 순서를 반대로 바꾼다
    - 만약 그 칸에 다른 말이 있으면, 다른 말들의 순서는 안바뀌고, 이동해서 그 칸으로 간 말들의 위치만 바뀐다
    A번 말이 이동하려는 칸이 파란색인 경우
    - A번 말의 이동방향을 반대로 하고 한 칸 이동한다 -> 파란색쪽으로 가서 바꾸는게 아니라 그 자리에서 바꾸는 거임
    - 만약 방향을 반대로 한 후 이동하려는 칸이 파란색일 경우에는 이동하지 않고, 방향만 반대로 바꾼다
    - 만약 칸을 벗어나면 파란색 칸을 만났다고 생각하고 하면 된다

    턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다, 만약에 1000턴 후에도 종료를 안하면 -1을 출력해라

    1 동, 2 서, 3 북, 4 남

    말은 번호가 낮은 말부터 순서대로 이동한다

    새로운 게임과 비슷하지만, 새로운 게임은 가장 아래있는 말만 이동하지만, 이것은 아님 -> 자기 보다 위에 있는 말과 함께 이동함
"""

N, K = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(N)]
piece_info = [[0]]
for _ in range(K):
    x, y, d = map(int, input().split())
    piece_info.append([x - 1, y - 1, d])


def state_init() -> list:
    """ 초기 상태를 정의해 주는 함수 """
    temp = [[[] for _ in range(N)] for _ in range(N)]
    cnt = 1
    for x, y, d in piece_info[1:]:
        temp[x][y].extend([cnt])
        cnt += 1

    return temp


def sep_area() -> tuple:
    """ 체스판에서 각각의 색이 어디에 있는지 확인해 주는 함수 """
    red_board = set()
    blue_board = set()

    for x in range(N):
        for y in range(N):
            if chess[x][y] == 1:
                red_board.add((x, y))

            elif chess[x][y] == 2:
                blue_board.add((x, y))

    return red_board, blue_board


def change_loc(arr, nx, ny) -> None:
    """ 각각의 위치(인덱스 값)를 바꾸어 주는 함수 """
    for idx in arr:
        piece_info[idx][0] = nx
        piece_info[idx][1] = ny


def decide_move(state, x, y, loc):
    """ 움직이는 블록이 무엇인지 알려주는 함수 """
    temp = []

    while True:
        if len(state[x][y]) == loc:
            break

        temp.append(state[x][y].pop(loc))

    return temp


def stand_red(state, x, y, nx, ny, idx):
    """ 빨간 땅을 밟았을 때 """
    loc = state[x][y].index(idx)
    temp = decide_move(state, x, y, loc)

    state[nx][ny].extend(list(reversed(temp)))
    change_loc(state[nx][ny], nx, ny)

    if len(state[nx][ny]) >= 4:
        return True


def stand_blue(state, x, y, d, idx, red_area, blue_area):
    """ 파란 땅을 밟았을 때 """
    change_d = [0, 2, 1, 4, 3]
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    d = change_d[d]

    nx = x + dx[d]
    ny = y + dy[d]
    piece_info[idx][2] = d

    if (nx, ny) in red_area:
        return stand_red(state, x, y, nx, ny, idx)

    elif not (0 <= nx < N and 0 <= ny < N) or (nx, ny) in blue_area:
        return False

    else:
        return stand_white(state, x, y, nx, ny, idx)


def stand_white(state, x, y, nx, ny, idx):
    """ 흰 땅을 밟았을 때 """
    loc = state[x][y].index(idx)
    temp = decide_move(state, x, y, loc)

    state[nx][ny].extend(temp)
    change_loc(state[nx][ny], nx, ny)

    if len(state[nx][ny]) >= 4:
        return True


def moving():
    """ 움직이는 함수 """
    state = state_init()
    red_area, blue_area = sep_area()

    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    time = 0

    while True:
        if time == 1000:
            return -1

        time += 1

        # print(*state, sep='\n')
        # print(f"{piece_info[1][2]} {piece_info[2][2]} {piece_info[3][2]} {piece_info[4][2]}")
        # print()

        for idx in range(1, K + 1):
            x = piece_info[idx][0]
            y = piece_info[idx][1]
            d = piece_info[idx][2]

            nx = x + dx[d]
            ny = y + dy[d]

            if (nx, ny) in red_area:
                if stand_red(state, x, y, nx, ny, idx):
                    return time

            elif not (0 <= nx < N and 0 <= ny < N) or (nx, ny) in blue_area:
                if stand_blue(state, x, y, d, idx, red_area, blue_area):
                    return time

            else:
                if stand_white(state, x, y, nx, ny, idx):
                    return time


print(moving())


"""
        핵심 정리
    1. 새로운 게임(17780번)과 비슷하지만, 이게 조금 더 어려움
    2. 그냥 하라는 대로 하면 되는 구현 문제지만, 은근히 실수 하기 쉬운 문제라서 천천히 정확하게 푸는게 좋음
"""
