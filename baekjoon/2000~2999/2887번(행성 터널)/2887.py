"""
    문제 이름 : 행성 터널
    URL : https://www.acmicpc.net/problem/2887
    ----------------------------------------------
    <문제 설명>
    각각의 행성을 연결하는 터널을 만들고 싶다
    각각의 터널의 좌표가 주어진다 (x, y, z)
    각가의 터널을 연결하는 비용은 min(|x1 - x2|, |y1 - y2|, |z1 - z2|)이다
    이 때, 모든 터널을 연결하는데 필요한 최소 비용을 출력해라
"""
N = int(input())
tunnel = []
for idx in range(1, N + 1):
    a, b, c = map(int, input().split())
    tunnel.append([a, b, c, idx])
connected_planet = [x for x in range(N + 1)]


def show_arr(arr):
    """ arr를 보여주는 함수 """
    print(*arr, sep='\n')
    print()


def sort_idx(arr, idx):
    """ 각각의 인덱스로 정렬을 한 후 현재 위치와 한 칸 앞 위치의 거리를 구해주는 함수 """
    temp = sorted(arr, key=lambda x: x[idx])

    return_arr = []

    for loc in range(len(temp) - 1):
        x = temp[loc][idx]
        nx = temp[loc + 1][idx]
        x_idx = temp[loc][3]
        nx_idx = temp[loc + 1][3]

        return_arr.append([x_idx, nx_idx, abs(x - nx)])

    return return_arr


def connect_planet(arr):
    """ 행성을 연결해 주는 함수 """
    arr.sort(key=lambda x: x[2])
    result = 0

    for node_1, node_2, cost in arr:
        if find(node_1) != find(node_2):
            union(node_1, node_2)
            result += cost

    return result


def find(node):
    """ 부모노드를 찾아주는 함수 """
    if connected_planet[node] == node: return node

    p = find(connected_planet[node])
    connected_planet[node] = p
    return p


def union(node_1, node_2):
    """ 두 노드를 합쳐주는 함수 """
    node_1 = find(node_1)
    node_2 = find(node_2)

    if node_1 > node_2:
        connected_planet[node_1] = node_2
    else:
        connected_planet[node_2] = node_1


def main():
    """ 함수를 실행 시켜줄 함수 """
    final_arr = sort_idx(tunnel, 0) + sort_idx(tunnel, 1) + sort_idx(tunnel, 2)
    result = connect_planet(final_arr)
    return result


print(main())

"""
        소요 시간
    40분 조금 더 걸림
    
        핵심 정리
    1. 모든 노드로 정렬을 해서 다 시간을 구하면 하나의 좌표를 구하는데 시간 복잡도가 O(N!)이 되어버림 => 당연히 시간 초과
    2. 이 문제는 각각의 좌표로 정렬을 해서 현재 위치와 한 칸 앞위치의 거리를 구하면 됨
    2-1. 정렬을 했기 때문에 현재 위치와 한 칸 앞의 위치의 거리를 당연히 최소 위치를 가짐
    3. 2번에서 구한 리스트로 MST를 하면 됨
"""