"""
    문제 이름 : 새로운 게임
    URL : https://www.acmicpc.net/problem/17780
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

    ==> 가장 아래있는 말만 이동할 수 있다

    턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다, 만약에 1000턴 후에도 종료를 안하면 -1을 출력해라

    1 동, 2 서, 3 북, 4 남

    말은 번호가 낮은 말부터 순서대로 이동한다
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


def change_loc(arr, nx, ny):
    for idx in arr:
        piece_info[idx][0] = nx
        piece_info[idx][1] = ny


def moving():
    """ 움직이는 함수 """
    state = state_init()
    red_area, blue_area = sep_area()

    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    change_d = [0, 2, 1, 4, 3]
    time = 0

    while True:
        if time >= 1000:
            return -1
        time += 1

        for idx in range(1, K + 1):

            x = piece_info[idx][0]
            y = piece_info[idx][1]
            d = piece_info[idx][2]

            if state[x][y][0] != idx:
                continue

            nx = x + dx[d]
            ny = y + dy[d]

            # 빨간 땅을 밟을 때
            if (nx, ny) in red_area:
                state[nx][ny].extend(list(reversed(state[x][y])))
                state[x][y] = []
                change_loc(state[nx][ny], nx, ny)

            # 파란 땅을 밟을 때
            if not (0 <= nx < N and 0 <= ny < N) or (nx, ny) in blue_area:
                d = change_d[d]
                nx = x + dx[d]
                ny = y + dy[d]

                if (nx, ny) in red_area:
                    state[nx][ny].extend(list(reversed(state[x][y])))
                    state[x][y] = []
                    piece_info[idx][2] = d
                    change_loc(state[nx][ny], nx, ny)

                if not (0 <= nx < N and 0 <= ny < N) or (nx, ny) in blue_area:
                    continue

                state[nx][ny].extend(state[x][y])
                piece_info[idx][2] = d
                state[x][y] = []
                change_loc(state[nx][ny], nx, ny)

            # 흰땅을 밟았을 때
            state[nx][ny].extend(state[x][y])
            state[x][y] = []
            change_loc(state[nx][ny], nx, ny)

            if len(state[nx][ny]) >= 4:
                return time


print(moving())


"""
        핵심정리
    1. 그냥 하라는 대로 하면 되는 문제
    2. 빡쎈 구현은 아니지만 상당히 귀찮은 구현이 많은 것 같은 문제
"""
