"""
    문제 이름 : 멀티탭 스케줄링
    URL : https://www.acmicpc.net/problem/1700
    ----------------------------------------------
    <문제 설명>
    멀티탭에 구멍의 개수와 사용하는 물품이 순서를 가지고 주어진다
    이 때, 하나씩 플러그를 빼는 최소의 횟수를 구해라
"""
from collections import deque

hole, things = map(int, input().split())
order_things = deque(map(int, input().split()))
cnt = 0


def state_init():
    """ 현재 상태를 구해주는 함수 """
    next_state = deque()

    while True:
        if len(order_things) == 0:
            break

        if len(next_state) == hole:
            break

        multitab = order_things.popleft()

        if order_things and order_things[0] == multitab:
            multitab = order_things.popleft()

        if multitab not in next_state:
            next_state.append(multitab)

    return next_state


def count_put(pre_state):
    """ 꽂아 준 것 횟수를 세주는 함수 """
    global cnt

    if len(order_things) == 0:
        return

    multitab = order_things.popleft()

    if multitab in pre_state:
        count_put(pre_state)
        return

    if len(order_things) == 0:
        if multitab not in pre_state:
            cnt += 1
        return

    pulled_thing = pull_thing(pre_state)

    for idx in range(len(pre_state)):
        if pre_state[idx] == pulled_thing:
            pre_state[idx] = multitab
            cnt += 1

    count_put(pre_state)


def pull_thing(pre_state):
    """ 뽑을게 무엇인지 알려주는 함수 """
    temp_index = 0
    temp_set = set()
    temp_state = pre_state

    for index in range(len(order_things)):
        for state_index in range(len(pre_state)):
            thing = order_things[index]
            state = pre_state[state_index]

            if thing == state and thing not in temp_set:
                temp_set.add(thing)
                if temp_index < index:
                    temp_index = index

    for x in range(len(temp_state)):
        if temp_state[x] not in temp_set:
            return temp_state[x]

    return order_things[temp_index]


def main():
    """ 함수를 실행 시켜줄 함수 """
    # 초기값
    pre_state = state_init()
    count_put(pre_state)


main()
print(cnt)


"""
        소요 시간
    3시간 걸림..... 어렵다 어려워~~
    
        핵심 정리
    1. 바꾸는 기준을 알면 됨
    1-1. 가장 늦게 재등장 하는 것
    1-2. 아예 등장하지 않는 것 -> 아예 등장하지 않는게 여러개면 아무거나 상관없음
    위 기준만 알고 풀면 쉬운데, 이걸 생각하는게 어려웠음
"""

