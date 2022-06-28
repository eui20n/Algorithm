"""
    문제 이름 : ACM Craft
    URL : https://www.acmicpc.net/problem/1005
    ----------------------------------------------
    <문제 설명>
    위상 정렬로 시간을 구하면 되는데, 많이 걸리는걸 기준으로 잡고 시간을 구하면 된다
"""
from collections import deque


def find_zero(cnt_build) -> list:
    """ 0을 찾아주는 함수 -> 시작점을 찾아주는 함수 """
    temp = cnt_build
    result = []

    for x in range(len(temp)):
        if temp[x] == 0:
            result.append(x)

    return result


def topology_sort(start, graph) -> list:
    """ 위상 정렬을 해줄 함수로 순서를 기록해줄 함수 """

    q = deque()
    result = [0] * (N + 1)

    for x in start:
        result[x] = build_time[x]
        q.append([x, x])

    while q:
        p = q.popleft()

        for x in graph[p[0]]:
            cnt_build[x] -= 1
            result[x] = max(result[p[0]] + build_time[x], result[x])
            if cnt_build[x] == 0:
                q.append([x, p[0]])

    return result


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    build_time = list(map(int, input().split()))
    build_time = [0] + build_time
    graph = [[] for _ in range(N + 1)]
    cnt_build = [0] * (N + 1)
    cnt_build[0] = False
    for _ in range(K):
        a, b = map(int, input().split())
        cnt_build[b] += 1
        graph[a].append(b)
    win_num = int(input())

    # print('cnt_build: ', cnt_build)
    # print('graph: ', graph)
    # print('build_time: ', build_time)

    start = find_zero(cnt_build)
    print(topology_sort(start, graph)[win_num])

# 각 건물이 지어지는데 얼마나 걸리는지 계속해서 적으면 되고 출력은 알고 싶은 건물이 얼마나 걸리는지 인덱스 번호로 접근해서 출력하면 됨
# 이전 인덱스를 저장해서 그 이전 값은 이전 인덱스 값 저장하기
# 각각의 인덱스는 해당 건물을 짓기 까지 걸리는 시간을 의미함
