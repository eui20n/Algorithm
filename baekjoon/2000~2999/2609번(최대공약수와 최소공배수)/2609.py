"""
    문제 이름 : 최대공약수와 최소공배수
    URL : https://www.acmicpc.net/problem/2609
    ----------------------------------------------
    <문제 설명>
    두 자연수를 입력받을 때, 최대공약수와 최소공배수를 출력하면 됨
"""


def find_num(num_1, num_2):
    """ 최대 공약수를 찾아주는 함수 """
    while num_2 != 0:
        t = num_1 % num_2
        num_1, num_2 = num_2, t

    return num_1


if __name__ == "__main__":
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a

    result = find_num(a, b)
    print(result, int(a * b / result), sep="\n")
