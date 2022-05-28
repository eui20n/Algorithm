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
sys.setrecursionlimit(10**5)

R, C = map(int, sys.stdin.readline().split())
lake = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
swan_loc = []


def find_swan():
    """ 호수의 위치를 찾아주는 함수 """
    for x in range(R):
        for y in range(C):
            if lake[x][y] == 'L':
                swan_loc.append([x, y])


def visited_init():
    """ 방문 처리 리스트를 생성해 주는 함수 """
    visited = [0] * C
    return visited


def melt_ice(x, y, visited):
    """ 녹는지 안녹는지 확인해주는 함수 """
    visited[y] |= (1 << x)

    if lake[x][y] == '.' or lake[x][y] == 'L':
        return []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append([x, y])

    temp_ice = []

    while q:
        x, y = q.popleft()

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue

            if lake[nx][ny] == '.' or lake[nx][ny] == 'L':
                temp_ice.append([x, y])
                continue

            if visited[ny] & (1 << nx):
                continue

            q.append([nx, ny])
            visited[ny] |= (1 << nx)

    return temp_ice


def check_melt():
    """ 어느 얼음이 녹는지 확인해 주는 함수 """
    visited = visited_init()

    melted_ice = []

    for x in range(R):
        for y in range(C):
            if not visited[y] & (1 << x):
                if temp := melt_ice(x, y, visited):
                    melted_ice.extend(temp)

    return melted_ice


def melting_ice(): # 이거 실행하기
    """ 얼음을 녹일 함수 """
    melted_ice = check_melt()

    for x, y in melted_ice:
        lake[x][y] = '.'


melting_ice()
print(*lake, sep='\n')



# 호수가 있는 칸 옆에 있는 빙판은 녹을까? -> 녹는다고 생각하고 하기

