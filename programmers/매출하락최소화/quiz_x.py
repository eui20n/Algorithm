"""
    문제 이름 : 매출 하락 최소화
    URL : https://school.programmers.co.kr/learn/courses/30/lessons/72416?language=python3
    ----------------------------------------------
    <문제 설명>
    각각의 직원 및 사장은 일련 번호를 가지고 있고, 팀에 소속되어 있음
    또한, 각 직원의 매출 정보도 주어짐
    직원들 중 몇명이 워크숍에 가야할 때 매출의 하락을 최소화 하고 싶다
    이 때, 최소화된 매출을 출력해라
    사장의 일련번호는 1번이다
    또한, 모든 직원은 1개의 팀에 속해있으며 워크숍에는 팀원중 한명은 무조건 가야함
    팀은 부모 노드와 직계 자식 노드 이다

"""

# 1 번 케이스
# sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
# links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]

# 2번 케이스
# sales = [5, 6, 5, 3, 4]
# links = [[2, 3], [1, 4], [2, 5], [1, 2]]

# 3번 케이스
# sales = [5, 6, 5, 1, 4]
# links = [[2, 3], [1, 4], [2, 5], [1, 2]]

# 4번 케이스
# sales = [10, 10, 1, 1]
# links = [[3, 2], [4, 3], [1, 4]]


def main(sale, link):
    """ 함수를 실행시켜줄 함수 """
    new_link = change_link(link)
    dp_table = [[0, 0] for _ in range(len(sale))]
    visited = [False for _ in range(len(sale))]
    tree_dp(sale, new_link, dp_table, visited, 1)
    print(dp_table)
    return min(dp_table[1])


def change_link(link):
    """ links를 보기 좋게 바꿔주는 함수 """
    new_link = [[] for _ in range(len(link) + 2)]

    # 문제에서 node_1이 부모 노드이고 node_2가 자식 노드라고 함
    for node_1, node_2 in link:
        new_link[node_1].append(node_2)

    return new_link


def tree_dp(sale, new_link, dp_table, visited, idx):
    """ tree_dp를 하는 함수 """
    visited[idx] = True

    if len(new_link[idx]) == 0:
        dp_table[idx][0] = sale[idx]
        dp_table[idx][1] = 0
        return

    for next_idx in new_link[idx]:
        if visited[next_idx] == True:
            continue

        tree_dp(sale, new_link, dp_table, visited, next_idx)

        # 자식 노드가 리프 노드 일때
        if len(new_link[next_idx]) == 0:
            pass
        # 자식 노드가 리트 노드가 아닐때
        else:
            pass



# def solution(sales, links):
#     answer = main([0] + sales, links)
#     return answer


main([0] + sales, links)
