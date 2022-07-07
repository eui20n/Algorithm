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


def check_loc():
    """ 시작, 끝, 물건 위치를 구해주는 함수 """
    start = []
    end = []
    cnt = 0

    for x in range(R):
        for y in range(C):
            if house[x][y] == 'S':
                house[x][y] = '.'
                start += [x, y]

            elif house[x][y] == 'E':
                house[x][y] = '.'
                end += [x, y]

            elif house[x][y] == 'X':
                house[x][y] = str(2 ** cnt)
                cnt += 1

    return start, end, cnt


def visited_init(cnt):
    """ 방문처리 리스트를 초기화 해주는 함수 """
    visited = [[[False] * C for _ in range(R)] for _ in range(2 ** cnt)]
    return visited


def search_house(start, end, things):
    """ 집을 탐색해주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = visited_init(things)
    visited[0][start[0]][start[1]] = True

    q = deque()
    q.append([start[0], start[1], 0, 0])

    while q:
        x, y, cnt, time = q.popleft()

        if x == end[0] and y == end[1] and cnt == 2 ** things - 1:
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
            if visited[cnt][nx][ny]:
                continue

            if house[nx][ny].isnumeric():
                house_num = int(house[nx][ny])
                if not cnt & house_num:
                    q.append([nx, ny, cnt | house_num, time + 1])
                    visited[cnt][nx][ny] = True
                    continue

            q.append([nx, ny, cnt, time + 1])
            visited[cnt][nx][ny] = True


def main():
    """ 함수를 실행 시켜줄 함수 """
    start, end, cnt = check_loc()
    result = search_house(start, end, cnt)
    return result


print(main())


"""
        소요 시간
    1시간 30분 정도 소요됨

        핵심정리
    1. 각각의 물건에 라벨을 붙여줌 => 2 ** 물건의 번호 (물건의 번호는 0 부터 시작) ==> 비트마스킹을 하기 위해서
    2. 해당 물건을 먹으면 해당 방문처리로 감
    3. 2 ** 물건의 개수 - 1 과 끝점과 x, y 가 같아지면 종료하면 됨
    4. 이 문제를 풀 때, 물건을 만나고 방문처리 리스트를 초기화 하는 식으로 하면 안됨 => 방향에 따라서 어느 물건은 늦게 만나는 경우가 생김
    4-1. 위 문제가 생기면 그 경로는 최단 경로가 아니게 됨 
"""