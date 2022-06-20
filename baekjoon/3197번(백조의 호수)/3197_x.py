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


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False] * C for _ in range(R)]
    return visited


def find_swan():
    """ 백조의 위치를 찾아주는 함수 """
    for x in range(R):
        for y in range(C):
            if lake[x][y] == 'L':
                yield [x, y]


def lake_in_swan(visited):
    """ 각각의 백조가 있는 호수를 묶어 주고 다음에 녹을 얼음이 무엇인지 알려주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    swan_1, swan_2 = find_swan()

    q = deque()
    swan_1_set = set()
    swan_2_set = set()
    melting_1 = set()
    melting_2 = set()

    for x, y in [swan_1, swan_2]:
        visited[x][y] = True

        if [x, y] == swan_1:
            q.append([x, y, '1'])
            swan_1_set.add((x, y))
        else:
            q.append([x, y, '2'])
            swan_2_set.add((x, y))

    while q:
        x, y, check = q.popleft()
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
                if check == '1':
                    melting_1.add((nx, ny))
                elif check == '2':
                    melting_2.add((nx, ny))

                continue

            if check == '1':
                swan_1_set.add((nx, ny))

            elif check == '2':
                swan_2_set.add((nx, ny))

            q.append([nx, ny, check])
            visited[nx][ny] = True

    return swan_1_set, swan_2_set, melting_1, melting_2


def first_melting_ice_no_swan(x, y, visited):
    """ 백조가 없는 호수에 뭐가 녹을지 알려주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = True

    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 > nx or nx >= R:
            continue
        if 0 > ny or ny >= C:
            continue
        if lake[nx][ny] == 'X':
            yield [nx, ny]


def first_melting_ice():
    """ 가장 처음 녹는 얼음을 구해주는 함수 """
    visited = visited_init()

    swan_1_set, swan_2_set, melting_1, melting_2 = lake_in_swan(visited)
    melting_ice = []

    for x in range(R):
        for y in range(C):
            if not visited[x][y] and lake[x][y] != 'X':
                melting_ice.extend(list(first_melting_ice_no_swan(x, y, visited)))

    return swan_1_set, swan_2_set, melting_1, melting_2, melting_ice


def next_melting(melting_1, melting_2, melting_ice):
    """ 다음에 녹을 얼음이 무엇인지 알려주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    temp_melting_1 = set()
    temp_melting_2 = set()
    temp_melting_ice = set()

    for x, y in melting_1:
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if lake[nx][ny] == 'X':
                temp_melting_1.add((nx, ny))

    for x, y in melting_2:
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if lake[nx][ny] == 'X':
                temp_melting_2.add((nx, ny))

    for x, y in melting_ice:
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if lake[nx][ny] == 'X':
                temp_melting_ice.add((nx, ny))

    return temp_melting_1, temp_melting_2, temp_melting_ice


def fun_melt(swan_1_set, swan_2_set, melting_1, melting_2, melting_ice):
    """ 녹여주는 함수 """
    for x, y in melting_ice:
        lake[x][y] = '.'

    for x, y in melting_1:
        lake[x][y] = '.'
        swan_1_set.add((x, y))

    for x, y in melting_2:
        lake[x][y] = '.'
        swan_2_set.add((x, y))


def melting():
    """ 녹여주는 함수 """
    time = 1
    swan_1_set, swan_2_set, melting_1, melting_2, melting_ice = first_melting_ice()
    fun_melt(swan_1_set, swan_2_set, melting_1, melting_2, melting_ice)

    while True:
        melting_1, melting_2, melting_ice = next_melting(melting_1, melting_2, melting_ice)
        fun_melt(swan_1_set, swan_2_set, melting_1, melting_2, melting_ice)
        time += 1


# print(first_melting_ice())
# print(melting())
print(melting())
# print(*lake, sep='\n')

# 이제 만나는 연산만 하면 됨 -> 집합을 이용해야함
# 중간에 물이 있으면 그 물은 아무 소속이 아니라서 인식을 못함 -> 이걸 해결하면 됨, 유니온 파인드가 맞는듯
# 아니면 다음 위치를 탐색할때, 다음 위치가 물인 곳이면 그냥 집합에 넣기
