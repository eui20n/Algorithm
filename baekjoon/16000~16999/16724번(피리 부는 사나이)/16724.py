"""
    문제 이름 : 피리 부는 사나이
    URL : https://www.acmicpc.net/problem/16724
    ----------------------------------------------
    <문제 설명>
    사람들이 방향 주어진 방향으로 움직인다. 사람들이 너무 움직이면 힘드니 쉼터를 만드려고 한다.
    이 때, 쉼터 개수의 최소값은 몇인가?
    방향
    U -> 위, D -> 아래, L -> 왼쪽, R -> 오른쪽
"""
R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]


def parent_node():
    """ 부모 노드를 설정해 주는 함수 """
    parent = {}
    for r in range(R):
        for c in range(C):
            parent[(r, c)] = (r, c)

    return parent


def find(parent, node):
    """ 부모 노드를 찾아주는 함수 """
    if parent[node] == node: return node

    p = find(parent, parent[node])
    parent[node] = p
    return p


def union(node_1, node_2, parent):
    """ 두 노드를 합쳐주는 함수 """
    node_1 = find(parent, node_1)
    node_2 = find(parent, node_2)

    if node_1 > node_2:
        parent[node_1] = node_2

    else:
        parent[node_2] = node_1


def make_safe_zone(parent):
    """ 몇개의 safe zone이 필요한지 알려주는 함수 """
    d = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
    result = 0

    for x in range(R):
        for y in range(C):
            nx_d = board[x][y]
            nx = x + d[nx_d][0]
            ny = y + d[nx_d][1]

            now_parent = find(parent, (x, y))
            next_parent = find(parent, (nx, ny))
            if now_parent != next_parent:
                union((x, y), (nx, ny), parent)

            elif now_parent == next_parent:
                result += 1

    return result


def show_arr(arr):
    """ 배열을 보기 쉽게 출력해주는 함수 """
    print(*arr, sep='\n')


def main():
    """ 함수를 실행 시켜줄 함수 """
    parent = parent_node()
    result = make_safe_zone(parent)
    return result


print(main())


"""
        소요 시간
    40분 정도 걸린 듯
    
        핵심 정리(Disjoint set으로 했지만 dfs도 동일할 것으로 예상함)
    1. 다시 자기 위치가 나오면 그 곳에 safe_zone을 만들면 됨
    2. 그리고 반복문은 딱 배열 한번만 돌아야함
    => 다시 자기 위치가 오는 것을 확인하고, 다른 곳을 확인할 땐, 이미 확인한 곳은 갈 필요 없음
"""