"""
        백준 https://www.acmicpc.net/problem/19911 문제를 사용함

        클래스로 구현한게 아니고, 그냥 구현을 한 것
"""


def preorder(node):
    """ 전위 순회 """

    # 들어가기 전에 출력을 함
    print(node, end="")

    left_node = tree[node][0]
    right_node = tree[node][1]

    if left_node != ".":
        preorder(left_node)
    if right_node != ".":
        preorder(right_node)


def inorder(node):
    """ 중위 순회 """
    left_node = tree[node][0]
    right_node = tree[node][1]

    if left_node != ".":
        inorder(left_node)

    # 왼쪽으로 끝까지 간 후, 그 시점의 왼쪽부터 출력함
    print(node, end="")

    if right_node != ".":
        inorder(right_node)


def postorder(node):
    """ 후위 순회 """
    left_node = tree[node][0]
    right_node = tree[node][1]

    if left_node != ".":
        postorder(left_node)
    if right_node != ".":
        postorder(right_node)

    # 아예 끝에서 부터 출력을 함 => 자식 노드가 없는 곳부터 출력한다고 생각하면 됨
    print(node, end="")


if __name__ == "__main__":
    N = int(input())

    tree = {}
    for _ in range(N):
        parent_node, child_node_1, child_node_2 = map(str,  input().split())
        tree[parent_node] = (child_node_1, child_node_2)

    preorder("A")
    print()
    inorder("A")
    print()
    postorder("A")
