"""
    문제 이름 : 휴게소 세우기
    URL : https://www.acmicpc.net/problem/1477
    ----------------------------------------------
    <문제 설명>
    현재 고속도로에 휴게소가 N개 있는데, M개를 더 세우려고 한다.
    휴게소는 휴게소가 있는 곳에는 세울 수 없고, 고속도로 끝에도 휴게소를 세울 수 없다.
    이 고속도로를 이용할 때, 모든 휴게소를 방문한다. 이 때, 휴게소가 없는 구간의 길이의 최대값을 최소로 하려고 한다. => M개 모두 지어야 한다
"""
N, M, L = map(int, input().split())
rest_area = [0] + list(map(int, input().split())) + [L]
rest_area.sort()


def check_build(num):
    """ 건설할 수 있는지 확인해주는 함수로, num보다 더 큰 구간이 있으면 안됨 """
    temp_list = [x for x in rest_area]
    cnt = 0
    idx = 0

    while True:
        if cnt > M:
            break

        end_con = True

        for x in range(idx, len(temp_list) - 1):
            dist = temp_list[x + 1] - temp_list[x]
            if dist > num:
                temp_list.append(temp_list[x] + num)
                temp_list.sort()
                idx = x + 1
                cnt += 1
                end_con = False
                break

        if end_con:
            break

    if cnt > M:
        return False
    else:
        return True


def binary_search(start, end):
    """ 이분 탐색을 해주는 함수 """
    while True:
        if start >= end:
            break

        mid = (start + end) // 2
        check = check_build(mid)

        if check:
            end = mid
        else:
            start = mid + 1

    return end


def main():
    """ 함수를 실행시켜주는 함수 """
    result = binary_search(0, L)
    return result


print(main())

"""
        핵심 정리
    1. 이분 탐색 정말 어렵다
    2. 우리가 구하고 싶은 것 => 최대 중 최소 이다. 이것을 그래프로 먼저 그려보면 뭘 구해야 할지 명확해진다
    => 하계 구하면 됨
    3. 미리 답을 고정 시키고, 구하면 되는데, 조건에 만족하면 고정된 답을 바꿔주면 된다
    => 답을 고정 시킨다는 개념보다는 범위가 있다는 개념이 이해하기 쉬움
"""

