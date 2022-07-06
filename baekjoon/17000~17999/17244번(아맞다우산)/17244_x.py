"""
    문제 이름 : 아맞다우산
    URL : https://www.acmicpc.net/problem/17244
    ----------------------------------------------
    <문제 설명>
    집에서 가지고 나와야 하는 물건이 좌표로 주어지고, 이 물건들을 최단 경로로 가지고 나오고 싶을 때, 최단경로는 몇인가
"""
from collections import deque

C, R = map(int, input().split())
house = [list(map(str, input())) for _ in range(R)]


def visited_init(cnt):
    """ 방문처리 리스트를 초기화 해주는 함수 """
    visited = [[0] * C for _ in range(2 ** cnt + 1)]
    return visited


def check_loc():
    """ 물건, 시작점, 도착점의 위치를 확인해주는 함수 """
    start = []
    end = []
    cnt = 0
    for x in range(R):
        for y in range(C):
            if house[x][y] == 'S':
                house[x][y] = '.'
                start+= [x, y]

            elif house[x][y] == 'E':
                house[x][y] = '.'
                end += [x, y]

            elif house[x][y] == 'X':
                cnt += 1
                house[x][y] = str(cnt)

    return start, end, cnt


def search_house(start, end, visited, things):
    """ 집을 탐색하는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[0][start[1]] |= (1 << start[0])

    q = deque()
    q.append([start[0], start[1], 0, 0])

    while q:
        x, y, cnt, time = q.popleft()

        if x == end[0] and y == end[1] and cnt == things:
            return time

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if house[nx][ny] == '#':
                continue
            if visited[cnt][ny] & (1 << nx):
                continue

            if house[nx][ny].isnumeric():
                house_num = int(house[nx][ny])

                if not cnt & house_num:
                    new_cnt = cnt + house_num
                    q.append([nx, ny, new_cnt, time + 1])
                    visited[new_cnt][ny] |= (1 << nx)
                    continue

            q.append([nx, ny, cnt, time + 1])
            visited[cnt][ny] |= (1 << nx)


def main():
    start, end, cnt = check_loc()
    visited = visited_init(cnt)
    return search_house(start, end, visited, cnt)


print(main())

# 먹은 라벨에 따라서 방문처리 리스트가 바꿔야함