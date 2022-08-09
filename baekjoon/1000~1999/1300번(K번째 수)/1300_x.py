"""
    문제 이름 : K번째 수
    URL : https://www.acmicpc.net/problem/1300
    ----------------------------------------------
    <문제 설명>
    N x N 크기의 A행렬이 있다. 이 행렬의 각각의 원소는 A[i][j] = i x j이다.
    이 때, 이 행렬을 일차원 배열에 넣은 후 오름차순 했을 때, K번째 수가 무언인지 출력해라
"""


def make_matrix():
    """ 행렬을 만들어 주는 함수 """
    arr = []
    for n in range(1, N + 1):
        temp = [x * n for x in range(1, N + 1)]
        arr.append(temp)

    return arr


def binary_search(start, end, arr):
    """ 이분탐색을 해주는 함수 """
    while True:
        if start >= end:
            break

        mid = (start + end) // 2
        check = big_or_small(mid, arr)


def big_or_small(num, arr):
    """ K번째 수보다 큰지 작은지 알려주는 함수 """
    pass




def main(arr):
    """ 함수를 실행시켜주는 함수 """
    binary_search(1, N ** 2, arr)


if __name__ == "__main__":
    N = int(input())
    K = int(input())
    matrix = make_matrix()


# 이렇게 하면 배열을 만드는 과정에서 최대 10^10임 => 시간 초과를 일으킴