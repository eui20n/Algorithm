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
    visited = [[False] * C for _ in range(R)]
    return visited


def find_cluster(): # 이거 실행
    """ 백조가 포함이 된 호수를 찾아주는 함수 """
    visited = visited_init()
    find_swan()
    swan_dict = {}

    for x, y in swan_loc:
        if not visited[x][y]:
            swan_dict[(x, y)] = swan_cluster(x, y, visited)

    return swan_dict


def swan_cluster(x, y, visited):
    """ 백조의 군집을 찾아주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = True

    temp_cluster = set([])

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
            if visited[nx][ny]:
                continue
            if lake[nx][ny] == 'X':
                continue

            q.append([nx, ny])
            visited[nx][ny] = True

            temp_cluster.add((nx, ny))
            lake[nx][ny] = 'L'

    return temp_cluster


def main():
    """ 함수를 실행 시켜줄 함수 """
    pass


swan_group = find_cluster()
print(swan_group)
print(*lake, sep='\n')

# 피리 부는 사나이 풀고 풀어보기