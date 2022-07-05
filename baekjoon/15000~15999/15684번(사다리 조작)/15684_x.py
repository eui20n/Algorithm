"""
    문제 이름 : 사다리 조작
    URL : https://www.acmicpc.net/problem/15684
    ----------------------------------------------
    <문제 설명>
    N개의 세로선, M개의 가로선이 있는 사다리가 있다
    각각의 세로선 마다 가로선을 놓을 수 있는 위치의 개수는 H이고, 모든 세로선이 같은 위치를 갖는다
    사다리 게임은 각각의 세로선마다 게임을 진행하고, 세로선의 가장 위에서부터 아래 방향으로 내려가야 한다
    이 때, 가로선을 만나면 가로선을 이용해 옆 세로선으로 이동한 다음 이동한 세로선에서 아래 방향으로 이동해야 한다

    우리는 가로선을 조작해서 i번 세로선이 i번으로 가게 하고 싶다
    이 때 조작해야 하는 가로선의 최소 수는 몇인가가
"""
import sys
from collections import deque
from copy import deepcopy

sys.setrecursionlimit(10 ** 6)

N, M, H = map(int, input().split())
ladder_info = []
for _ in range(M):
    a, b = map(int, input().split())
    ladder_info.append([a, b])

min_add_ladder = float('inf')


def change_ladder():
    """ ladder_info를 보고 좌표 평명 위로 바꿔주는 함수 """
    ladder = [[0] * N for _ in range(H)]
    # 구분을 하기 위해서 있음
    cnt = 1

    # a, b는 문제에서 주어진 입력
    for a, b in ladder_info:
        ladder_idx_1, ladder_idx_2 = b - 1, b
        ladder[a - 1][ladder_idx_1] = cnt
        ladder[a - 1][ladder_idx_2] = cnt
        cnt += 1

    return ladder, cnt


def all_combination(ladder):
    """ 사다리 타기 할 수 있는 모든 선 """
    temp = deque()
    all_case = []

    for x in range(H):
        for y in range(N - 1):
            temp.append([x, y, x, y + 1])

    for x, y, x_1, y_1 in temp:
        if ladder[x][y] != 0 and ladder[x][y] == ladder[x_1][y_1]:
            continue

        all_case.append([x, y, x_1, y_1])

    return all_case


def ladder_game(ladder, all_case, cnt, result, start):
    """ 사다리 타기 게임을 하는 함수 """
    global min_add_ladder

    if game(ladder):
        if min_add_ladder > result:
            min_add_ladder = result

    if start == len(all_case):
        return

    for idx in range(start, len(all_case)):
        x = all_case[idx][0]
        y = all_case[idx][1]
        x_1 = all_case[idx][2]
        y_1 = all_case[idx][3]

        ladder[x][y], ladder[x_1][y_1] = cnt + 1, cnt + 1
        ladder_game(ladder, all_case, cnt + 1, result + 1, idx + 1)
        ladder[x][y], ladder[x_1][y_1] = 0, 0


def game(ladder):
    """ 사다리 타기를 하는 곳"""
    for start in range(N):
        idx = start
        x = 0
        while True:
            if idx + 1 < N and ladder[x][idx] != 0 and ladder[x][idx] == ladder[x][idx + 1]:
                idx += 1

            elif idx - 1 >= 0 and ladder[x][idx] != 0 and ladder[x][idx] == ladder[x][idx - 1]:
                idx -= 1

            x += 1
            if x == H - 1:
                break

        if start == idx:
            continue
        else:
            return False

    return True


def main():
    """ 함수를 실행 시켜줄 함수 """
    ladder, cnt = change_ladder()
    all_case = all_combination(ladder)
    ladder_game(ladder, all_case, cnt, 0, 0)


main()
print(min_add_ladder)

# M의 가로선의 개수임, R와 C으로 볼꺼면 H과 N임
# 좌표로 표현하고 각각의 가로선을 구분지으면 됨

# change_ladder 내 생각 대로 나옴
# all_combination 내 생각 대로 나옴
