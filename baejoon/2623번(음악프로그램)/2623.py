"""
    문제 이름 : 음악프로그램
    URL : https://www.acmicpc.net/problem/2623
    ----------------------------------------------
    <문제 설명>
    어떤한 순서에 대해서 정렬을 하면됨, 여기서 어떠한 순서는 아직 모름 허허;
    위상정렬인데 각각의 다른 리스트에 대해서 위상정렬을 하면 될듯
    만약에 위상정렬이 불가능 하면 0을 출력하기 -> 사이클이 있으면 0 출력
"""
from collections import deque

N, M = map(int, input().split())
music = []
for _ in range(M):
    a = list(map(int, input().split()))
    music.append(a[1:])


def music_order_f():
    """ 위상 정렬 할 수 있게 각각이 뭐를 가르키는지 확인해주는 함수 """
    music_order = [[] for _ in range(N + 1)]
    for x in range(M):
        for y in range(len(music[x]) - 1):
            music_order[music[x][y]].append(music[x][y + 1])
    return music_order


def music_cnt_f():
    """ 몇번 선택이 되었는지 확인해주는 함수 """
    music_cnt = [0] * (N + 1)
    music_cnt[0] = 'x'

    for x in music_order_f():
        if len(x) == 0:
            continue
        for y in x:
            music_cnt[y] += 1
    return music_cnt


def find_start():
    """ 시작점을 찾아주는 함수 """
    start = []
    music_cnt = music_cnt_f()
    for x in range(1, len(music_cnt)):
        if music_cnt[x] == 0:
            start.append(x)
    return start


def topology_sort(start):
    """ 위상 정렬 함수 """
    q = deque(start)
    result = []
    cycle_check = set([])

    music_order = music_order_f()
    music_cnt = music_cnt_f()

    while q:
        p = q.popleft()
        result.append(p)
        if p in cycle_check:
            return 0
        else:
            cycle_check.add(p)

        for x in music_order[p]:
            music_cnt[x] -= 1
            if music_cnt[x] == 0:
                q.append(x)
    if len(result) == N:
        return result
    else:
        return 0


def main():
    """ 함수를 실행하는 함수 """
    start = find_start()
    result = topology_sort(start)
    return result


if main() == 0:
    print(0)
else:
    print('\n'.join(map(str, main())))

# print("music: ", music)
# print("music_order: ", music_order_f())
# print("music_cnt: ", music_cnt_f())
# # print("start: ", start)
