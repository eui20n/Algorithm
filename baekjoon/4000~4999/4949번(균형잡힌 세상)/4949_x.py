"""
    문제 이름 : 균형잡힌 세상
    URL : https://www.acmicpc.net/problem/4949
    ----------------------------------------------
    <문제 설명>
    문자열의 괄호가 잘 닫혀 있는지 확인하면 됨.
    괄호가 잘 닫히면 균형잡힌 것임
"""


def check(arr):
    """ 균형잡혀 있는지 확인해주는 함수 """
    result = []

    for word in arr:
        if word != "(" and word != ")" and word != "[" and word != "]":
            continue

        if word == "(":
            result.append(word)
        elif word == ")" and result and result[-1] == "(":
            result.pop()
        elif word == ")" and not result:
            result.append(word)

        if word == "[":
            result.append(word)
        elif word == "]" and result and result[-1] == "[":
            result.pop()
        elif word == "]" and not result:
            result.append(word)

    if result:
        return "no"
    else:
        return "yes"


while True:
    sentence = list(input())
    if sentence == ["."]:
        break

    print(check(sentence))

