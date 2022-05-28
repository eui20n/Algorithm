"""
    문제 이름 : 중량제한
    URL : https://www.acmicpc.net/problem/1939
    ----------------------------------------------
    <문제 설명>
    다리에 중량 제한이 있는데, 한번에 옮길수 있는 물건의 최대 중량을 구해라
"""
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(M + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start, end = map(int, input().split())


print(f"N : {N},M : {M}")
print("graph")
print(*graph, sep='\n')
print(f"start : {start}, end : {end}")

# 이분탐색 하고 하기