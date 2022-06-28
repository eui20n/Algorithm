"""
    문제 이름 : 욕심쟁이 판다
    URL : https://www.acmicpc.net/problem/1937
    ----------------------------------------------
    <문제 설명>
    판다는 본인이 있는 위치에서 대나무가 더 많은 곳으로 이동한다
    이 때, 판다가 이동할 수 있는 경우의 최대값을 구해라
"""
import sys
sys.setrecursionlimit(10**6)

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]

go_panda_cnt = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def go_panda(x, y):
    """ 판다가 움직이는 함수 """
    if x >= N or y >= N:
        return

    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 > nx or nx >= N:
            continue
        if 0 > ny or ny >= N:
            continue
        if forest[x][y] >= forest[nx][ny]:
            continue
        if go_panda_cnt[nx][ny] != 0:
            go_panda_cnt[x][y] = max(go_panda_cnt[x][y], go_panda_cnt[nx][ny] + 1)
            continue

        go_panda_cnt[x][y] = max(go_panda_cnt[x][y], go_panda(nx, ny) + 1)

    if go_panda_cnt[x][y] == 0:
        go_panda_cnt[x][y] = 1

    return go_panda_cnt[x][y]


def main():
    """ 함수를 실행 시킬 함수 """
    for x in range(N):
        for y in range(N):
            if go_panda_cnt[x][y] == 0:
                go_panda(x, y)

    max_num = 0
    for x in range(N):
        for y in range(N):
            if max_num < go_panda_cnt[x][y]:
                max_num = go_panda_cnt[x][y]

    return max_num


print(main())


"""
        소요 시간
    1시간 30분 정도 소요함
    
        핵심 정리
    1. dfs + dp 문제로 생각이 엄청나게 많이 필요함
    2. 문제 잘 읽자 -> 큰 쪽으로 가야하는데, 크거나 같은 쪽으로 가는 걸로 풀어서 안됬네
    3. 2번의 연장선으로, 메모리 초과가 뜨는 이유가 많은데 보통은 스택 오버플로우임 => 재귀, 스택, 큐 와 같은 것들이 계속 들어가는 현상
"""
