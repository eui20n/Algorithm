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
cut_wood_num = 0


def binary_search(start, end):
    """ 이분 탐색 함수 """
    global cut_wood_num
    if start > end:
        return end

    mid = (start + end) // 2
    num = cutting_wood(mid)

    if num <= M:
        return binary_search(start, mid - 1)
    else:
        return binary_search(mid + 1, end)


def cutting_wood(num):
    """ 나무를 잘라주는 함수 """
    cutting_num = 0

    for height in tree_height:
        if num < height:
            cutting_num += height - num

    return cutting_num


def main():
    """ 함수를 실행 시켜주는 함수 """
    return binary_search(1, max(tree_height))


print(main())

