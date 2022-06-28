"""
    문제 이름 : 청소년 상어
    URL : https://www.acmicpc.net/problem/19236
    ----------------------------------------------
    <문제 설명>
    크기는 4 x 4 고정, 각 칸에 물고기가 방향과 번호를 가지고 있다 -> 1 <= 번호 <= 16, 번호가 같은 물고기는 없다
    방향은 8방향 -> 상하좌우, 대각선
    초기 위치 (0,0)
    순서
    1. 상어가 물고기를 먹는다 -> 상어는 먹은 물고기의 방향을 가지고 있다
    2. 물고기가 이동한다 -> 한칸 이동
    2-1. 번호가 작은 물고기 부터 순서대로 이동함, 이동은 빈 칸과 다른 물고기가 있는 칸, 이동 못하는 칸은 상어가 있거나 범위를 벗어나는 칸
    2-2. 만약에 현재 방향에서 이동을 못하면 이동이 가능할때까지 45도 반시계 회전함, 그래도 이동할 칸이 없으면 이동 안함
    2-3. 그 외 경우에는 이동하는데, 그 칸에 물고기와 자리를 바꾸는 방식으로 이동함
    3. 상어 이동 -> 여러 칸 이동가능
    3-1. 만약 물고기가 있는 칸으로 이동했으면 그 칸의 물고기를 먹고 그 방향을 얻음
    3-2. 물고기가 없는 칸으로는 이동할 수 없다
    3-3. 이동할 칸이 없으면 종료

    상어가 먹을 수 있는 번호의 총합의 최대값을 구해라

    북(1): x - 1, y
    북서(2): x - 1, y - 1
    서(3): x, y - 1
    남서(4): x + 1, y - 1
    남(5): x + 1, y
    남동(6): x + 1, y + 1
    동(7): x, y + 1
    북동(8): x - 1, y + 1
"""
from copy import deepcopy

fish_num = [[] for _ in range(4)]
fish_dir_temp = [[] for _ in range(4)]

for column in range(4):
    a = list(map(int, input().split()))

    for idx in range(len(a)):
        if idx % 2 == 0:
            fish_num[column].append(a[idx])

        else:
            fish_dir_temp[column].append(a[idx])

fish_dir = [0] * 17
for x in range(4):
    for y in range(4):
        fish_dir[fish_num[x][y]] = fish_dir_temp[x][y]

shark_r = 0
shark_c = 0
shark_d = fish_dir[fish_num[0][0]]
shark_score = fish_num[0][0]

fish_dir[fish_num[0][0]] = 0
fish_num[0][0] = -1

global result
result = 0


def fish_move(go_fish, fish_list, fish_dir_list):  # 이거 실행하면 됨
    """ 물고기가 이동하는 함수 """
    if go_fish == 17:
        return
    break_true = False  # 이거 어거지임, 이거 말고 다른 방법 있으면 그거 쓰기, 근데 이거 쓰면 맞긴함 -> 일단 맞추자..!

    #  생각할 것 -> 물고기가 없을 수도 있음
    for x in range(4):
        for y in range(4):
            if fish_list[x][y] == go_fish:
                # 물고기 방향보고 이동
                change_fish_loc(x, y, go_fish, 1, fish_list, fish_dir_list)
                break_true = True
                break
        if break_true:
            break

    fish_move(go_fish + 1, fish_list, fish_dir_list)  # 핵심은 이거 위치임, 이거 위치로 위의 반복문 전체가 멈춰야 함


def change_fish_loc(x, y, fish, cnt, fish_list, fish_dir_list):
    """ 물고기의 위치를 바꿔주는 함수 """
    if cnt == 9:
        return

    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

    go_fish_dir = fish_dir_list[fish]

    # 재귀 들어가기
    for z in range(1, 9):
        if go_fish_dir == z:
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 <= nx < 4 and 0 <= ny < 4 and fish_list[nx][ny] != -1:
                fish_list[nx][ny], fish_list[x][y] = fish_list[x][y], fish_list[nx][ny]
                return

            if go_fish_dir == 8:
                fish_dir_list[fish] = 1
            else:
                fish_dir_list[fish] += 1

            change_fish_loc(x, y, fish, cnt + 1, fish_list, fish_dir_list)


def shark_move(x, y, d, fish_list, fish_dir_list, score):  # 상어 x, y, 방향, 물고기 리스트, 점수
    """ 상어가 이동하는 함수 """
    global result

    # 여기서 재귀가 일어남
    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

    if score > result:
        result = score

    nx_1 = x + dx[d]
    ny_1 = y + dy[d]
    nx_2 = x + dx[d] * 2
    ny_2 = y + dy[d] * 2
    nx_3 = x + dx[d] * 3
    ny_3 = y + dy[d] * 3

    for nx, ny in [[nx_1, ny_1], [nx_2, ny_2], [nx_3, ny_3]]:
        if 0 <= nx < 4 and 0 <= ny < 4 and fish_list[nx][ny] != 0:
            temp_score = score

            fish_temp_list = deepcopy(fish_list)
            fish_temp_dir = deepcopy(fish_dir_list)

            d = fish_temp_dir[fish_temp_list[nx][ny]]
            fish_temp_dir[fish_temp_list[nx][ny]] = 0

            temp_score += fish_temp_list[nx][ny]

            fish_temp_list[nx][ny] = -1
            fish_temp_list[x][y] = 0

            fish_move(1, fish_temp_list, fish_temp_dir)
            shark_move(nx, ny, d, fish_temp_list, fish_temp_dir, temp_score)


def main(fish_list, fish_dir_list):
    """ 함수를 실행 시켜줄 함수 """

    fish_list = deepcopy(fish_list)
    fish_dir_list = deepcopy(fish_dir_list)

    fish_move(1, fish_list, fish_dir_list)
    shark_move(shark_r, shark_c, shark_d, fish_list, fish_dir_list, shark_score)


main(fish_num, fish_dir)
print(result)

"""
        문제 정리
1. 재귀를 정말 많이 사용함 -> 내가 문제풀면서 이만큼 재귀를 사용해 본적이 없음
2. 재귀를 쓸때 deepcopy와 전역변수 안쓰고 하기 -> 아직 실력이 부족해서 못함
3. 특별히 어려운 로직은 없음
4. 재귀를 쓰니까 각 함수의 역할 및 끝나는 조건 등을 확실히 알아야함, 이거만 유의하면서 풀면 쉬움

"""