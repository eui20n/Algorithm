"""
    문제 이름 : 2048 - hard
    URL : https://www.acmicpc.net/problem/12094
    ----------------------------------------------
    <문제 설명>
    2048 - easy의 어려운 버전으로, easy는 최대 5번을 움직여서 최대값을 구하는 거라면, hard는 최대 10번 움직여서 최대값을 구하는 문제

    시간을 엄청나게 잘 써야함
"""

from copy import deepcopy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

global result
result = 0


def move_left(arr):
    """ 왼쪽으로 움직이는 함수 """
    # 한번 합해지면 스탑하고 다른 거라고 인식하기
    for x in range(N):
        cnt = 0
        for y in range(1, N):
            if arr[x][y] == 0:
                continue

            if arr[x][cnt] == arr[x][y]:
                arr[x][cnt] += arr[x][y]
                arr[x][y] = 0
                cnt += 1

            elif arr[x][cnt] != arr[x][y]:
                if arr[x][cnt] == 0:
                    arr[x][cnt] = arr[x][y]
                    arr[x][y] = 0

                else:
                    cnt += 1
                    if cnt == y: continue

                    arr[x][cnt] = arr[x][y]
                    arr[x][y] = 0

    return arr


def move_right(arr):
    """ 오른쪽으로 움직이는 함수 """
    for x in range(N):
        cnt = N - 1
        for y in range(N - 2, -1, -1):
            if arr[x][y] == 0:
                continue

            if arr[x][cnt] == arr[x][y]:
                arr[x][cnt] += arr[x][y]
                arr[x][y] = 0
                cnt -= 1

            elif arr[x][cnt] != arr[x][y]:
                if arr[x][cnt] == 0:
                    arr[x][cnt] = arr[x][y]
                    arr[x][y] = 0

                else:
                    cnt -= 1
                    if cnt == y: continue

                    arr[x][cnt] = arr[x][y]
                    arr[x][y] = 0

    return arr


def move_up(arr):
    """ 위로 움직이는 함수 """
    for y in range(N):
        cnt = 0
        for x in range(1, N):
            if arr[x][y] == 0:
                continue

            if arr[cnt][y] == arr[x][y]:
                arr[cnt][y] += arr[x][y]
                arr[x][y] = 0
                cnt += 1

            elif arr[cnt][y] != arr[x][y]:
                if arr[cnt][y] == 0:
                    arr[cnt][y] = arr[x][y]
                    arr[x][y] = 0

                else:
                    cnt += 1
                    if cnt == x: continue

                    arr[cnt][y] = arr[x][y]
                    arr[x][y] = 0

    return arr


def move_down(arr):
    """ 아래로 움직이는 함수 """
    for y in range(N):
        cnt = N - 1
        for x in range(N - 2, -1, -1):
            if arr[x][y] == 0:
                continue

            if arr[cnt][y] == arr[x][y]:
                arr[cnt][y] += arr[x][y]
                arr[x][y] = 0
                cnt -= 1

            elif arr[cnt][y] != arr[x][y]:
                if arr[cnt][y] == 0:
                    arr[cnt][y] = arr[x][y]
                    arr[x][y] = 0

                else:
                    cnt -= 1
                    if cnt == x: continue

                    arr[cnt][y] = arr[x][y]
                    arr[x][y] = 0

    return arr


def game_2048(board, cnt):
    """ 2048을 해주는 함수 -> 최대값을 구해주는 함수 """
    global result

    if cnt == 5:
        max_num = find_max_num(board)
        if max_num > result:
            result = max_num
        return

    temp = deepcopy(board)

    temp_left = move_left(deepcopy(board))
    temp_right = move_right(deepcopy(board))
    temp_up = move_up(deepcopy(board))
    temp_down = move_down(deepcopy(board))

    # print('temp_left')
    # print(*temp_left, sep = '\n')
    # print('temp_right')
    # print(*temp_right, sep = '\n')
    # print('temp_up')
    # print(*temp_up, sep = '\n')
    # print('temp_down')
    # print(*temp_down, sep = '\n')

    total_temp = [temp_left, temp_right, temp_up, temp_down]

    for check_list in total_temp:
        if check_list == temp:
            max_num = find_max_num(check_list)

        else:
            game_2048(check_list, cnt + 1)
            continue

        if max_num > result:
            result = max_num


def find_max_num(arr):
    """ 최대값을 찾아주는 함수 """
    temp = 0

    for x in range(N):
        for y in range(N):
            if arr[x][y] > temp:
                temp = arr[x][y]

    return temp


# print("---- move_left ----")
# print(*move_left(deepcopy(board)), sep='\n')
# print("---- move_right ----")
# print(*move_right(deepcopy(board)), sep='\n')
# print("---- move_up ----")
# print(*move_up(deepcopy(board)), sep='\n')
# print("---- move_down ----")
# print(*move_down(deepcopy(board)), sep='\n')

game_2048(board, 0)
print(result)

# return 사용해서 풀기