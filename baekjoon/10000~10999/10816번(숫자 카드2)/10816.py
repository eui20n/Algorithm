"""
    문제 이름 : 숫자 카드2
    URL : https://www.acmicpc.net/problem/10816
    ----------------------------------------------
    <문제 설명>
    숫자가 주어질 때, 이 숫자가 몇번 등장하는지 출력하면 됨
"""
N = int(input())
num_card = list(map(int, input().split()))
M = int(input())
com_card = list(map(int, input().split()))


def make_dict():
    """ 해시와 맵 생성해주는 함수 """
    temp_dict = {}
    for x in com_card:
        temp_dict[x] = 0

    return temp_dict


def main():
    """ 함수를 실행시켜줄 함수 """
    com_dict = make_dict()
    key = set(com_dict.keys())

    for x in num_card:
        if x not in key:
            continue
        com_dict[x] += 1

    for x in com_card:
        print(com_dict[x], end=" ")


main()
