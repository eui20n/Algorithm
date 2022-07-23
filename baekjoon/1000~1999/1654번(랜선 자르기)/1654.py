"""
    문제 이름 : 랜선 자르기
    URL : https://www.acmicpc.net/problem/1654
    ----------------------------------------------
    <문제 설명>
    K개의 랜선의 길이는 제각각이다. 이 K개의 랜선을 N개로 서로 같은 크기로 만들고 싶어서 K개의 랜선을 자르려고 한다.
    => N개 보다 많이 만드는 것도 N개에 포함된다.
    이 때 만들 수 있는 랜선의 최대 길이를 구해라.
"""
K, N = map(int, input().split())
lan = []
for _ in range(K):
    weight = int(input())
    lan.append(weight)


def binary_search(start, end):
    """ 이분 탐색을 해주는 함수 """
    if start > end:
        return end

    mid = (start + end) // 2
    cnt = cut_lan(mid)

    if cnt >= N:
        return binary_search(mid + 1, end)
    else:
        return binary_search(start, mid - 1)


def cut_lan(num):
    cnt = 0

    for weight in lan:
        cnt += weight//num

    return cnt


def main():
    """ 함수를 실행 시켜줄 함수 """
    return binary_search(1, max(lan))


print(main())

"""
        이분 탐색
    1. 너무 생각을 많이 해야한다.
    2. 머리가 상당히 아프다.
"""