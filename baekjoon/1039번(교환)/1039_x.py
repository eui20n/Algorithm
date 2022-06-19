"""
    문제 이름 : 교환
    URL : https://www.acmicpc.net/problem/1039
    ----------------------------------------------
    <문제 설명>
    정수 N이 있다. M을 N의 자릿수라고 할 때, 아래 연산을 K번 한다
    1 <= i < j <= M인 i와 j를 고른다. 그 다음, i번 위치의 숫자와 j번 위치의 숫자를 바꾼다. 이때, 바꾼 수가 0으로 시작하면 안된다
    위의 연산을 K번 했을 때, 나올 수 있는 수의 최대값을 구해라
    만약 연산을 k번 할 수 없으면 -1을 출력해라
"""
from collections import deque

num, K = map(int, input().split())

# 만약에 시간이 많이 걸리면 K를 문자열로 받고, 그것만 숫자로 변환해서 하기
# 이 문제 비트 마스킹으로 하기 -> 나중에 하자!
