"""
    문제 이름 : 큰 수 만들기
    URL : https://www.acmicpc.net/problem/16496
    ----------------------------------------------
    <문제 설명>
    음이 아닌 정수가 주어졌을 때, 해당 정수들로 만들 수 있는 가장 큰 수를 구해라
"""
N = int(input())
number = list(map(str, input().split()))
number.sort(key=lambda x:x[0])
print(number)