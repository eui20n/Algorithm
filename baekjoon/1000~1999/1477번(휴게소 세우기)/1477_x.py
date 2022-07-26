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
rest_area = list(map(int, input().split()))


def binary_search(start, end):
    """ 이분 탐색을 해주는 함수 """
    cnt = 0
    result = 0
    max_num = check_max(0)[0]

    while True:
        if cnt == M:
            break

        while True:
            if start >= end:
                rest_area.append(end)
                break

            mid = (start + end) // 2
            temp_num, bigger_num = check_max(mid)

            if bigger_num:
                start = mid + 1
            else:
                end = mid

            if max_num > temp_num:
                max_num = temp_num

        cnt += 1
        result = max_num

    return result


def check_max(num):
    """ 현재 구간에서 최대값을 구해주는 함수 """
    temp_list = [0] + rest_area + [L]

    if num != 0:
        temp_list.append(num)

    temp_list.sort()
    bigger_num = False

    cnt = 0
    for x in temp_list:
        if num == x:
            break
        cnt += 1

    max_num = 0
    for x in range(len(temp_list) - 1):
        temp_num = temp_list[x + 1] - temp_list[x]
        if max_num < temp_num:

            if cnt <= x and num != 0:
                bigger_num = True

            max_num = temp_num

    return max_num, bigger_num


def main():
    """ 함수를 실행시켜줄 함수 """
    result = binary_search(0, L)
    return result


print(main())
print(rest_area)
