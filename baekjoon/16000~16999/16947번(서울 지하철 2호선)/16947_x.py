"""
    문제 이름 : 서울 지하철 2호선
    URL : https://www.acmicpc.net/problem/16947
    ----------------------------------------------
    <문제 설명>
    각각의 역에서 순환선 까지 걸리는 시간을 구해라 -> 순환선 안에 있는 철로는 0이다
"""
from collections import deque

N = int(input())
subway = [[] for _ in range(N + 1)]
for _ in range(N):
    a, b = map(int, input().split())
    subway[a].append(b)
    subway[b].append(a)


print(subway)

# 간선의 개수와 정점의 개수가 같은 연결 그래프는 사이클을 정확히 하나만 갖는다....!
# => 이 문제는 간선 수와 정점의 수가 같다
