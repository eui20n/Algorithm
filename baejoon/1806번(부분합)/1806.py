"""
    문제 이름 : 부분합
    URL : https://www.acmicpc.net/problem/1806
    ----------------------------------------------
    <문제 설명>
    입력으로 주어진 부분합을 구하려고 할때, 그 부분합을 가장 짧게 만드는 경우 그 길이를 출력해라
"""

N, K = map(int, input().split())
num = list(map(int, input().split()))


def two_pointer(num, K):
    """ 투 포인터 함수로 원하는 부분합을 찾아주는 함수 """
    start = 0
    end = 0
    count = 1
    result = [0, float('inf')]  # 0번째 인덱스는 부분합, 1번째 인덱스는 그 때 길이

    for _ in range(len(num)):
        result[0] += num[end]
        end += 1
        count += 1

        while True:
            if result[0] < K or start == end:
                break

            result[0] -= num[start]
            count -= 1
            start += 1

            if result[1] > count:
                result[1] = count

    if result[1] >= float('inf'):
        return 0
    else:
        return result[1]


print(two_pointer(num, K))

# print(num)
