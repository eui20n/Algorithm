"""
    문제 이름 : 세계 정복
    URL : https://www.acmicpc.net/problem/1578
    ----------------------------------------------
    <문제 설명>
    세계정복을 위해서 N개의 국가를 정복했다. N개의 국가의 사람이 친하지 않음을 깨닫고 모든 사람들을 서로 친하게 만들어야 한다는 것을 알았다.
    이러기 위해서 사람들을 그룹으로 나누려고 한다. 방법은 다음과 같다.
    1. 그룹에 들어있는 수는 정확히 K명이어야 한다. 또, 각 그룹에 있는 사람들은 모두 다른 나라 소속이어야 한다.
    N개의 국가에 살고 있는 사람의 수가 주어졌을 때, 이 사람들을 최대 몇 개의 그룹으로 나눌 수 있는지 출력해라
    만약에 어느 그룹에도 들어가지 않는 사람이 있다면, 과감히 무시해라
"""


def binary_search(start, end):
    """ 이분탐색을 해주는 함수 """
    while True:
        if start >= end:
            break

        mid = (start + end) // 2
        check = check_sep(mid)

        if check:
            start = mid + 1
        else:
            end = mid

    return end - 1


def check_sep(num):
    """ num로 나눌 수 있는지 구해주는 함수로 num보다 커도 num로 나눌 수 있는 것 """
    cnt = 0
    temp_sum = 0
    for x in person:
        if x >= num:
            cnt += num
            continue
        temp_sum += x

    final_num = cnt + temp_sum

    if final_num >= K * num:
        return True
    else:
        return False


def main():
    """ 함수를 실행시켜주는 함수 """
    result = binary_search(1, sum(person)//K + 1)
    print(result)


if __name__ == "__main__":
    N, K = map(int, input().split())
    person = list(map(int, input().split()))
    person.sort(reverse=True)
    main()


"""
        핵심 정리
    1. 단순한 이분 탐색 문제라서 이분 탐색 조금만 할 줄 알아도 쉽게 해결가능함
    2. 문제는 시간복잡도를 생각해야하는 문제임, 범위를 줄이는 로직을 시간을 잘 신경써서 짜야함
"""