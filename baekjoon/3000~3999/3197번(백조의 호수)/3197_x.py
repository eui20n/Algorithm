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
swan_cluster = [[0] * C for _ in range(R)] # 백조의 군집을 나타내주는 리스트
visited_melting_ice = [0] * C # 얼음이 녹았던 곳을 표시해주는 곳 => 얼음이 녹을 때, 그 곳이 중복 선택이 되는 경우를 막기 위해서 만듬


def find_swan():
    """ 백조의 위치를 찾아주는 함수 """
    swan = []
    for x in range(R):
        for y in range(C):
            if lake[x][y] == 'L':
                swan.append([x, y])
                lake[x][y] = '.'
    return swan


def check_swan_cluster():
    """ 백조 구역을 정해주는 함수 """
    swan_1, swan_2 = find_swan()

    swan_cluster_bfs(swan_1[0], swan_1[1], 1)
    swan_cluster_bfs(swan_2[0], swan_2[1], 2)


def swan_cluster_bfs(x, y, cnt):
    """ 백조 구역을 표시해주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    swan_cluster[x][y] = cnt

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
            if lake[nx][ny] == 'X':
                continue
            if swan_cluster[nx][ny]:
                continue

            q.append([nx, ny])
            swan_cluster[nx][ny] = cnt


# 얼음에서 시작해서 물이랑 만나는 것이 녹는 것이라고 판단
def first_melting_ice():
    """ 제일 처음 녹을 얼음을 알려주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    swan_1 = [] # 백조의 구역이 1인 경우에서 녹는 경우
    swan_2 = [] # 백조의 구역이 2인 경우에서 녹는 경우
    temp = [] # 그 외 경우

    for x in range(R):
        for y in range(C):
            if lake[x][y] == '.': # 현재 위치가 물이면 건너 뜀
                continue

            # 얼음이면 4방향을 봐서 물이 있는지 확인 => 물이 있으면 녹는 얼음
            for z in range(4):
                nx = x + dx[z]
                ny = y + dy[z]
                if 0 > nx or nx >= R:
                    continue
                if 0 > ny or ny >= C:
                    continue
                if lake[nx][ny] == 'X':
                    continue

                # 녹을 얼음이니까 얼음을 방문처리 해줌 => (x, y)에 해주는 이유는 현재위치가 얼음일 때를 본 것이기 때문
                visited_melting_ice[y] |= (1 << x)

                # 구역이 1이면 1에 넣음
                if swan_cluster[nx][ny] == 1:
                    swan_1.append([x, y])

                # 구역이 2이면 2에 넣음
                elif swan_cluster[nx][ny] == 2:
                    swan_2.append([x, y])

                # 그 외는 그 외에 넣음
                else:
                    temp.append([x, y])
    # 이렇게 넣으면 처음에 녹는 얼음에 중복되는 것이 생기는데, 이는 처음이라서 중복을 허용했음 -> 이렇게 안하면 정확하지 않다고 생각
    return swan_1, swan_2, temp


# arr : 이번에 녹는 얼음, swan_kind : 몇 구역의 백조인지, swan_true : 백조가 있는 구역인지 아닌지
def find_melting_ice(arr, swan_kind, swan_true):
    """ 녹을 얼음을 찾아주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 이번에 녹은 얼음이 하나도 없으면 당연히 다음에 녹을 얼음도 없다는 의미
    if len(arr) == 0:
        return [], False

    # 다음에 녹을 얼음을 담을 리스트
    temp = []

    for x, y in arr:
        if swan_true:
            # 만약에 백조의 무리에서 녹은 얼음이면 두 무리가 만나는지 확인해줌
            if check_meet_swan(x, y, swan_kind):
                # 만난다면 리스트와 True를 반환해줌
                return temp, True

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if lake[nx][ny] == '.':
                continue
            if visited_melting_ice[ny] & (1 << nx):
                continue

            visited_melting_ice[ny] |= (1 << nx)
            temp.append([nx, ny])
    # 여기까지 왔다는 것은 백조가 안만났다는 것 => False 반환
    return temp, False


def melting_ice(arr, swan_kind):
    """ 얼음을 녹여줄 함수 """
    # 녹을 리스트를 받아서 녹여줌
    for x, y in arr:
        lake[x][y] = '.'
        swan_cluster[x][y] = swan_kind


def check_meet_swan(x, y, swan_kind):
    """ 백조가 만나는지 확인해주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

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
            if lake[nx][ny] == 'X':
                continue
            # 현재와 같은 군집이면 안감 => 방문처리를 하는 것
            if swan_cluster[nx][ny] == swan_kind:
                continue
            # 여기 까지 왔다면 남은건 군집이 없는 경우와 다른 군집인데, 여기서 군집이 없는건 0을 의미 => 0이 아니라는건 다른 군집을 만났다는 것
            # 이 경우는 종료 => True를 반환함
            if swan_cluster[nx][ny] != 0:
                return True

            q.append([nx, ny])
            swan_cluster[nx][ny] = swan_kind

    return False


def main():
    """ 함수를 실행 시켜줄 함수 """
    check_swan_cluster()
    swan_1, swan_2, temp = first_melting_ice()
    time = 0

    while True:
        # 녹이는 건 아무 구역도 아닌 곳을 먼저 녹여줌 => 그래야 백조가 서로 만난는지 찾을 때, 올바르게 찾을 수 있다고 생각
        time += 1
        melting_ice(temp, 0)
        melting_ice(swan_1, 1)
        melting_ice(swan_2, 2)

        # 녹는 얼음을 찾는건 백조가 있는 군집의 얼음부터 찾아줌 => 백조가 있는 얼음이 녹아야 bfs를 돌려서 서로 만날 수 있는지 확인할 수 있음
        swan_1, meet = find_melting_ice(swan_1, 1, True)
        if meet:
            return time

        swan_2, meet = find_melting_ice(swan_2, 2, True)
        if meet:
            return time

        temp, meet = find_melting_ice(temp, 0, False)


print(main())

