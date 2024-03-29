"""
    문제 이름 : 사회망 서비스(SNS)
    URL : https://www.acmicpc.net/problem/2533
    ----------------------------------------------
    <문제 설명>
    친구관계 트리가 주어졌을 때, 모든 사람들이 새로운 아이디어를 수용하기 위해서 필요한 최소 얼리 어답터의 수를 구해라
    사람들은 얼리 어답터 이거나 얼리 어답터가 아니다. 사람들은 자신의 모든 친구가 얼리어답터일 때, 새로운 아이디어를 받아들인다.
"""
import sys
sys.setrecursionlimit(1000000)


def dp(visited, dp_table, idx):
    """ dp를 해주는 함수 """
    visited[idx] = 1

    for next_idx in tree[idx]:
        if visited[next_idx]:
            continue

        dp(visited, dp_table, next_idx)

        # 현재 노드가 얼리 어답터 일 때
        dp_table[idx][0] += min(dp_table[next_idx][1], dp_table[next_idx][0])

        # 현재 노드가 얼리 어답터가 아닐 때
        dp_table[idx][1] += dp_table[next_idx][0]


def main():
    """ 함수를 실행시켜 주는 함수 """
    visited = [0 for _ in range(N + 1)]
    dp_table = [[1, 0] for _ in range(N + 1)]
    dp(visited, dp_table, 1)

    return min(dp_table[1])


if __name__ == "__main__":
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)

    # print(f"tree : {tree}")
    print(main())


"""
    앞으로 입력을 받을 때 sys.stdin.readline으로 받자
"""