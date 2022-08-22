"""
    문제 이름 : 우수 마을
    URL : https://www.acmicpc.net/problem/1949
    ----------------------------------------------
    <문제 설명>
    1번 부터 N번의 번호가 붙은 마을이 트리 구조로 되어있다.
    각 마을을 잇는 길이 있다. => 방향이 없다.
    모든 마을은 연결되어 있으며, 직접 연결되어 있으면 두 마을은 인접해 있다고 한다.
    이 마을 중에서 우수 마을을 아래 조건으로 선정하려고 한다.
    1. "우수 마을"로 선정된 마을 주민 수의 총 합을 최대로 해야 한다.
    2. 마을 사이의 충돌을 방지하기 위해서, "우수 마을" 두 마을이 인접해 있으면 두 마을을 모두 "우수 마을"로 선정할 수 없다.
       즉, "우수 마을"끼리 인접할 수 없다. => 부모 노드 or 자식 노드에는 우수 마을이 없다
    3. "우수 마을"로 선정되지 못한 마을 옆에는 "우수 마을"이 인접해 있다.
    우수 마을의 주민 수의 총합을 구해라

    우수 마을은 하나가 아니다.
"""
from sys import setrecursionlimit as limit
from collections import deque
limit(10**5)


def find_parent():
    """ 각 노드의 부모 노드를 찾아주는 함수 """
    parent_node = [0] * (N + 1)
    parent_node[1] = -1

    q = deque()
    q.append(1)

    while q:
        x = q.popleft()
        for nx in village[x]:
            if parent_node[nx] != 0:
                continue

            q.append(nx)
            parent_node[nx] = x

    return parent_node


def dp(visited, node_parent, dp_table, idx):
    """ 다이나믹 프로그래밍을 구현하는 함수 """
    visited[idx] = True

    if node_parent[idx] != -1 and len(village[idx]) == 1:
        dp_table[idx][0] = population[idx]
        return

    for next_idx in village[idx]:
        if visited[next_idx]:
            continue
        dp(visited, node_parent, dp_table, next_idx)

        dp_table[idx][0] = max(population[idx], dp_table[idx][0]) + dp_table[next_idx][1]

        dp_table[idx][1] = max(dp_table[next_idx][0], dp_table[next_idx][1]) + dp_table[idx][1]


def main():
    """ 함수를 실행시키는 함수 """
    visited = [False] * (N + 1)
    node_parent = find_parent()
    dp_table = [[0, 0] for _ in range(N + 1)]

    dp(visited, node_parent, dp_table, 1)

    return dp_table


if __name__ == "__main__":
    N = int(input())
    population = [0] + list(map(int, input().split()))
    village = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        village[a].append(b)
        village[b].append(a)

    print(max(main()[1]))

