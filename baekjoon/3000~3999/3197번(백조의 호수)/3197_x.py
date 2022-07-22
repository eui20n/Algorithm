"""
    문제 이름 : 백조의 호수
    URL : https://www.acmicpc.net/problem/3197
    ----------------------------------------------
    <문제 설명>
    매일 물과 접촉한 호수는 녹는다(대각선은 제외)
    백조는 세로나 가로로만 이동 가능할때 며칠이 지나야 백조들이 만날 수 있는지 구해라
    백조는 무조건 2마리이다
"""
from collections import deque
import sys

R, C = map(int, sys.stdin.readline().split())
lake = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
arr_sep_swan = [[0] * C for _ in range(R)]
melting_ice = [[False] * C for _ in range(R)]


def show_arr(arr):
    """ arr를 보기 좋게 출력해주는 함수 """
    print(*arr, sep='\n')


def find_swan():
    """ 백조의 위치를 찾아주는 함수 """
    swan = []
    for x in range(R):
        for y in range(C):
            if lake[x][y] == "L":
                swan.append([x, y])
                lake[x][y] = "."

    return swan


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False] * C for _ in range(R)]
    return visited


def sep_swan(x, y, visited, cnt):
    """ 백조의 구역을 나눠주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    arr_sep_swan[x][y] = cnt
    visited[x][y] = True

    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if lake[nx][ny] == "X":
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            q.append([nx, ny])
            arr_sep_swan[nx][ny] = cnt


def first_melting_ice(x, y):
    """ 처음에 녹을 얼음 """
    swan_1 = []
    swan_2 = []
    other = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 > nx or nx >= R:
            continue
        if 0 > ny or ny >= C:
            continue

        if lake[nx][ny] == '.' and not melting_ice[x][y]:
            if arr_sep_swan[nx][ny] == 1:
                swan_1.append([x, y])
            elif arr_sep_swan[nx][ny] == 2:
                swan_2.append([x, y])
            elif arr_sep_swan[nx][ny] == 0:
                other.append([x, y])

            melting_ice[x][y] = True

    if len(swan_1):
        return swan_1, 1
    elif len(swan_2):
        return swan_2, 2
    else:
        return other, 0


def find_first_melting_ice():
    """ 처음에 녹을 얼음을 찾아주는 함수 """
    swan_1 = []
    swan_2 = []
    other = []

    for x in range(R):
        for y in range(C):
            if lake[x][y] == "X":
                temp, num = first_melting_ice(x, y)
                if not temp:
                    continue

                if num == 1:
                    swan_1 += temp
                elif num == 2:
                    swan_2 += temp
                elif num == 0:
                    other += temp

    return swan_1, swan_2, other


def main():
    """ 함수를 실행시켜줄 함수 """
    #-------- 구역 정해줌 ----------------------
    swan_1, swan_2 = find_swan()
    visited = visited_init()
    sep_swan(swan_1[0], swan_1[1], visited, 1)
    sep_swan(swan_2[0], swan_2[1], visited, 2)
    #-----------------------------------------

    #------ 제일 처음 녹을 얼음 찾고 녹이기 -------
    ice_1, ice_2, ice_other = find_first_melting_ice()


main()
show_arr(arr_sep_swan)
