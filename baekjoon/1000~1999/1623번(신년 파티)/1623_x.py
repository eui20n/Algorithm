"""
    문제 이름 : 신년 파티
    URL : https://www.acmicpc.net/problem/1623
    ----------------------------------------------
    <문제 설명>
    사장이 루트 노드, 직원이 하위 노드이다.
    파티를 하려고 하는데, 부하직원과 그 직속상관이 같이 올 수 없다.
    또한, 위의 조건을 만족하면서 분위기를 최고로 높이려고 한다.
    분위기는 점수가 있는데 이를 최대로 하면 된다.
    이 때, 사장(루트 노드)가 있는 파티와 없는 파티의 분위기의 최대값을 출력해라
    또한, 누가 참석하는지도 출력해야한다.
"""


def new_year_party(visited, dp_table, join_list_o, join_list_x, idx):
    """ 신년 파티 -> DP함수 """
    visited[idx] = True

    for next_idx in tree[idx]:
        if visited[next_idx]:
            continue

        new_year_party(visited, dp_table, join_list_o, join_list_x, next_idx)

        dp_table[idx][0] = 1
        dp_table[idx][1] = 1



def main():
    """ 함수를 실행시켜줄 함수 """
    visited = [False for _ in range(N + 1)]
    dp_table = [[0, 0] for _ in range(N + 1)]

    # 참석 명단으로 사장이 있을 때랑 없을 때
    join_list_o = []
    join_list_x = []

    new_year_party(visited, dp_table, join_list_o, join_list_x, 1)


if __name__ == "__main__":
    N = int(input())
    score = list(map(int, input().split()))
    superior = list(map(int, input().split()))

    tree = [[] for _ in range(N + 1)]
    for x in range(len(superior)):
        tree[superior[x]].append(x + 2)

    main()

    print(f"tree : {tree}")
    print(f"superior : {superior}")
