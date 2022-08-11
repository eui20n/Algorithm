"""
    문제 이름 : 트리 순회
    URL : https://www.acmicpc.net/problem/19911
    ----------------------------------------------
    <문제 설명>
    이진 트리를 입력받아 전위 순회, 중위 순회, 후위 순회한 결과를 출력해라
"""


def preorder(node):
    """ 전위 순회 """
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
