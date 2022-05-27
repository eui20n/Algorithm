"""
    문제 이름 : 미네랄
    URL : https://www.acmicpc.net/problem/2933
    ----------------------------------------------
    <문제 설명>
    왼쪽과 오른쪽에서 번갈아가며 진행됨 -> 왼쪽 먼저
    막대나 미네랄을 만나면, 그 칸에 있는 미네랄은 모두 파괴되고 막대는 이동을 멈춤 -> 모두 파괴된다는게 그 칸에 있는 것을 의미 => 1개 파괴
    파괴된 미네랄이 떠있으면 바닥으로 떨어지는데, 이때 본인 군집의 모양은 유지가 된다
"""
from collections import deque

R, C = map(int, input().split())
cave = [list(map(str, input())) for _ in range(R)]
throw_count = int(input())
bar_height = list(map(int, input().split()))


def change_height():
    """ 단위를 바꿔주는 함수로 높이가 아래에서 시작해서 헷갈림 """
    for x in range(len(bar_height)):
        bar_height[x] = R - bar_height[x]


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False] * C for _ in range(R)]
    return visited


def throw_bar(height, order):  # 높이와 오른쪽인지 왼쪽인지 순서 입력
    """ 창을 던지는 함수 """
    if order == 'L':
        loc = 0
        direction = 1

    else:
        loc = C - 1
        direction = -1

    while True:
        if cave[height][loc] == 'x':
            cave[height][loc] = '.'
            break
        loc += 1 * direction

        if 0 > loc or loc >= C:
            break


def check_cluster(x, y, visited):
    """ 군집이 있는지 확인해 주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = True

    q = deque()
    q.append([x, y])

    cluster = [[x, y]]

    while q:
        x, y = q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if check_cluster_con(nx, ny, visited):
                q.append([nx, ny])
                visited[nx][ny] = True
                cluster.append([nx, ny])

    return cluster


def check_cluster_con(x, y, visited):
    """ check_cluter 의 조건 함수 """
    if 0 > x or x >= R:
        return False
    if 0 > y or y >= C:
        return False
    if cave[x][y] == '.':
        return False
    if visited[x][y]:
        return False
    return True


def find_floating_mineral():  # 군집 찾을 꺼면 이걸 실행 시키면 됨
    """ 떠있는 미네랄을 찾아주는 함수 """
    visited = visited_init()

    # 바닥에 붙어 있는 것을 먼저 확인 -> 그 후 확인 하면 그건 떠있는 거임
    for y in range(C):
        if not visited[R - 1][y]:
            check_cluster(R - 1, y, visited)

    # 이제 전체 확인 -> 공중에 동시에 2개의 군집이 있을 수가 없어서 하나 찾으면 바로 종료
    for x in range(R):
        for y in range(C):
            if cave[x][y] == '.':
                continue

            if not visited[x][y]:
                floating_cluster = check_cluster(x, y, visited)
                return floating_cluster

    return []


def gravity(floating_cluster):
    """ 중력을 적용해주는 함수 """
    # 한칸씩 내리면 될듯

    mineral_to_point(floating_cluster)

    floating_cluster.sort(key=lambda x: (x[1], -x[0]))
    mineral = False

    # 그냥 비우고 한칸씩 본다음에 만나면 멈추고 그 때의 값들로 다시 채워주면 될거 같음
    while True:
        temp = []

        for tmp in range(len(floating_cluster)):
            x = floating_cluster[tmp][0]
            y = floating_cluster[tmp][1]

            if x + 1 == R or cave[x + 1][y] == 'x':
                mineral = True
                break

            temp.append([x + 1, y])

        if mineral:
            break

        floating_cluster = temp

    point_to_mineral(floating_cluster)


def point_to_mineral(cluster_list):
    """ 점인 군집을 미네랄로 바꿔주는 함수 """
    for x, y in cluster_list:
        cave[x][y] = 'x'


def mineral_to_point(cluster_list):
    """ 군집을 점으로 바꾸기 """
    for x, y in cluster_list:
        cave[x][y] = '.'


def main():
    """ 함수를 실행 시킬 함수 """
    change_height()
    cnt = 0
    for x in bar_height:
        if cnt % 2 == 0:
            throw_bar(x, 'L')
        else:
            throw_bar(x, 'R')

        cnt += 1

        if floating_cluster := find_floating_mineral():
            gravity(floating_cluster)

    for x in cave:
        print(''.join(x))


main()