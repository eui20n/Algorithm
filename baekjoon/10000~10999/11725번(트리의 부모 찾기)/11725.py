"""
    문제 이름 : 트리의 부모 찾기
    URL : https://www.acmicpc.net/problem/11725
    ----------------------------------------------
    <문제 설명>
    1번 노드를 루트노드라고 할 때, 1번 노드를 제외한 노드들의 부모를 찾으면 됨
"""
from collections import deque


def find_parent(arr):
    """ 부모 노드를 찾아주는 함수 """
    q = deque()
    q.append(1)

    result = [0] * (N + 1)
    visited = [False] * (N + 1)
    visited[1] = True

    while q:
        x = q.popleft()
        for nx in arr[x]:
            if not visited[nx]:
                q.append(nx)
                result[nx] = x
                visited[nx] = True

    return result


if __name__ == "__main__":
    N = int(input())
    arr = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        node_1, node_2 = map(int, input().split())
        arr[node_2].append(node_1)
        arr[node_1].append(node_2)

    result = find_parent(arr)
    print(*result[2:], sep="\n")


