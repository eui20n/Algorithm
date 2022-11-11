"""
    문제 이름 : 통나무 자르기
    ----------------------------------------------
    <문제 설명>
    통나무를 자르는 게임을 하는데, 자연수로 더 이상 자를 수 없게 되면 짐
    이 때, 이긴 사람을 출력해라
"""


def game(length):
    if length % 2 == 0:
        return "Alice"
    else:
        return "Bob"


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        wood_length = int(input())
        result = game(wood_length)
        print(f"#{i} {result}")
