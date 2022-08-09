"""
    문제 이름 : 명령 프롬프트
    URL : https://www.acmicpc.net/problem/1032
    ----------------------------------------------
    <문제 설명>
    문자열이 주어지는데, 이 문자열의 패턴을 파악하면 됨
"""
N = int(input())
words = []
for _ in range(N):
    words.append(list(input()))

result = words[0]

for word in words:
    for idx in range(len(word)):
        if result[idx] != word[idx]:
            result[idx] = "?"

print("".join(result))
