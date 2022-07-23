"""
    문제 이름 : 나무 자르기
    URL : https://www.acmicpc.net/problem/2805
    ----------------------------------------------
    <문제 설명>
    높이가 H보가 높은 나무는 짤린다 => 그럼 나무를 나무의 높이 - H 만큼 얻을 수 있다
    이 때, 나무 M미터를 가져가기 위한 H의 최대값을 구해라
"""
N, M = map(int, input().split())
tree_height = list(map(int, input().split()))


def binary_search(start, end):
    """ 이분 탐색을 해주는 함수 """
    if start > end:
        return end

    mid = (start + end) // 2
    num = cutting_wood(mid)

    if num >= M:
        return binary_search(mid + 1, end)
    else:
        return binary_search(start, mid - 1)


def cutting_wood(num):
    """ 나무를 잘라주는 함수 """
    cutting_num = 0

    for height in tree_height:
        if num < height:
            cutting_num += height - num

    return cutting_num


def main():
    """ 함수를 실행 시켜주는 함수 """
    result = binary_search(0, max(tree_height))
    return result


print(main())


"""
        이분 탐색 + 매개 변수 탐수
    1. 어렵다
    2. 생각할 것이 너무 많은 듯
"""
