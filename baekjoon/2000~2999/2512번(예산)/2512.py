"""
    문제 이름 : 예산
    URL : https://www.acmicpc.net/problem/2512
    ----------------------------------------------
    <문제 설명>
    가능한 최대 총 예산은 다음과 같은 방법으로 배정함
    1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
    2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
       상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.

    위 두 조건을 만족하여 예산을 줄 때, 받는 예산의 최대값을 구해라
"""


def binary_search(start, end):
    """ 이분 탐색을 진행해주는 함수 """
    while True:
        if start >= end:
            break

        mid = (start + end) // 2
        check_num = check_budget(mid)

        if total_budget >= check_num:
            start = mid + 1
        else:
            end = mid

    return end


def check_budget(budget):
    """ 예산을 num로 했을 때, 총 예산이 얼마인지 알려주는 함수 """
    num = 0
    for x in require_budget:
        if x > budget:
            num += budget
        else:
            num += x

    return num


def main():
    """ 함수를 실행 시켜주는 함수 """
    budget = binary_search(1, total_budget)
    result = 0
    for x in require_budget:
        if x >= budget:
            result = budget - 1
            break
        elif result < x:
            result = x

    return result


if __name__ == "__main__":
    N = int(input())
    require_budget = list(map(int, input().split()))
    total_budget = int(input())
    sum_budget = sum(require_budget)

    print(main())
