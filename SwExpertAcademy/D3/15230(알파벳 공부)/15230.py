"""
    문제 이름 : 알파벳 공부
    ----------------------------------------------
    <문제 설명>
    문자열이 주어질 때, 이 문자열이 알파벳 순서와 얼마나 맞는지 출력하면 됨
"""


def check(string):
    result = 0
    check_words = "abcdefghijklmnopqrstuvwxyz"

    loop_num = min(len(string), len(check_words))

    for idx in range(loop_num):
        if check_words[idx] != string[idx]:
            break
        result += 1

    return result


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        word = input()
        ans = check(word)
        print(f"#{i} {ans}")
