"""
    문제 이름 : 공유기 설치
    URL : https://www.acmicpc.net/problem/2110
    ----------------------------------------------
    <문제 설명>
    C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 구해라
    => 최소가 최대가 되는 경우를 구해라 -> 상계
"""
house_num, ip_time = map(int, input().split())
house = []
for _ in range(house_num):
    temp_input = int(input())
    house.append(temp_input)
house.sort()


def check_iptime(num):
    """ 인접한 공유기 사이 거리 """
    idx = 0
    cnt = 1
    for x in range(1, len(house)):
        dist = house[x] - house[idx]
        if dist > num:
            idx = x
            cnt += 1

    if cnt < ip_time:
        return False
    else:
        return True


def binary_search(start, end):
    """ 이분 탐색을 해주는 함수 """
    while True:
        if start >= end:
            break

        mid = (start + end) // 2
        check = check_iptime(mid)

        if check:
            start = mid + 1
        else:
            end = mid

    return end


def main():
    """ 함수를 실행시켜주는 함수 """
    return binary_search(0, 1000000000)


print(main())

"""
        핵심 정리
    1. 이분 탐색 어렵다
    2. 이분 탐색을 할 때는, 원본 리스트를 건드리는게 아니라 범위를 건드려야함
    3. 이분 탐색을 하는 과정에서 범위를 신경 잘 써야함
    4. 결정 문제로 계속해서 질문을 던져야함
"""