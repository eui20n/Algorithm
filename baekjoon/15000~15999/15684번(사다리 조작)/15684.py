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
N, M, H = map(int, input().split())
ladder_info = []
for _ in range(M):
    a, b = map(int, input().split())
    ladder_info.append([a - 1, b - 1])

min_add_ladder = float('inf')


def change_ladder_info():
    """ ladder info를 가지고 그래프로 나타내기 """
    temp = [[0] * N for _ in range(H)]
    cnt = 1
    for a, b in ladder_info:
        temp[a][b] = cnt
        temp[a][b + 1] = cnt
        cnt += 1

    return temp, cnt


def all_combination(ladder):
    """ 현재 발판이 있는 경우를 제외한 모든 경우의 수 """
    temp = []
    for x in range(H):
        for y in range(N - 1):
            x_1, y_1, x_2, y_2 = x, y, x, y + 1
            if ladder[x_1][y_1] == 0 and ladder[x_2][y_2] == 0:
                temp.append([x_1, y_1, x_2, y_2])
    return temp


def ladder_game(ladder, all_case, cnt, result, start):
    """ 사다리 타기 게임 - 재귀 부분"""
    global min_add_ladder

    if result >= 4:
        return

    if game(ladder):
        if min_add_ladder > result:
            min_add_ladder = result

    for idx in range(start, len(all_case)):
        x = all_case[idx][0]
        y = all_case[idx][1]
        x_1 = all_case[idx][2]
        y_1 = all_case[idx][3]

        if ladder[x][y] == 0 and ladder[x_1][y_1] == 0:
            ladder[x][y], ladder[x_1][y_1] = cnt, cnt
            ladder_game(ladder, all_case, cnt + 1, result + 1, idx + 1)
            ladder[x][y], ladder[x_1][y_1] = 0, 0


def game(ladder):
    """ 사다리 타기 게임 - 게임 부분 """
    for start in range(N):
        idx = start
        x = 0

        while True:
            if idx + 1 < N and ladder[x][idx] != 0 and ladder[x][idx] == ladder[x][idx + 1]:
                idx += 1

            elif idx - 1 >= 0 and ladder[x][idx] != 0 and ladder[x][idx] == ladder[x][idx - 1]:
                idx -= 1

            x += 1
            if x == H and idx != start:
                return False

            if x == H and idx == start:
                break

    return True


def main():
    """ 함수를 실행 시켜줄 함수 """
    ladder, cnt = change_ladder_info()
    all_case = all_combination(ladder)
    ladder_game(ladder, all_case, cnt, 0, 0)

    if min_add_ladder == float('inf') or min_add_ladder > 4:
        return -1
    return min_add_ladder


print(main())


"""
        핵심 정리
    1. 이문제는 실수가 엄청나게 많았음
    1-1. 문제를 안읽음 => 최대로 추가 되는 사다리는 3개임, 그 이상은 볼 필요 없었음
    1-2. 세로선은 연속해서 있을 수 없었음
    1-3. 위 2개를 몰라서(문제를 잘 안읽어서) 한참걸림
    1-4. 1-1에서 최대로 추가되는 사다리는 3개인데, 4개로 계산해서 답이 계속 틀렸다고 나옴
    1-5. 실수를 좀 줄이고 문제를 잘 읽어야함
    
    2. 사다리가 추가될 수 있는 모든 곳을 구한다음 그 경우로 백트래킹(조합)을 하면 됨
"""