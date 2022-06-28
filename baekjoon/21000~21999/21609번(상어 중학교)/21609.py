"""
    문제 이름 : 상어 중학교
    URL : https://www.acmicpc.net/problem/21609
    ----------------------------------------------
    <문제 설명>
    N x N에 여러개 색의 블록이 있다 -> 검은(1), 무지개(0), 일반(M 이하의 자연수)
    인접한 칸 개념 |r1 - r2| + |c1 - c2| = 1 을 만족하는 칸 -> 상하좌우
    인접한 블록을 블록 집합이라고 함 -> 색이 모두 같은 일반 블록 적어도 1개, 검은 블록은 없고, 무지개 블록은 얼마 든지 있어도 된다
    블록 집합에 속한 블록의 개수는 2보다 크거나 같고, 집합 안에서 어디든지 이동 가능해야 한다
    블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록
    블록 그룹이 존재하는 동안 아래 행동이 반복된다
    1. 크기가 가장 큰 블록 그룹을 찾는다. 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 그러한 블록도 여러개라면
       기준 블록의 행이 가장 큰것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
    2. 1 에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B^2점을 획득한다.
    3. 격자의 중력이 작용한다.
    4. 격자가 90도 반시계 방향으로 회전한다.
    5. 다시 격자에 중력이 작용한다.

    중력이 작용하면 검은 색 블록을 제외하고 모두 아래로 내려가는데, 과정 중에 검은 색 블록이 있으면 검은색 블록 위로 간다

    귀찮은거 많이 시키는 문제구만 허허;;
    시간 측정하지 말고 zip을 활용해서 회전 구현하기 -> 그래도 가능하면 3시간 잡고 하기
    깊이 우선 탐색으로 간다! -> 못갈듯
"""
from collections import deque

N, Color = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False] * N for _ in range(N)]
    return visited


def find_block_group(x, y, visited, game_board):
    """ 블록 그룹을 찾아주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited_0 = visited_init()
    visited_0[x][y] = True

    q = deque()
    q.append([x, y])

    color = game_board[x][y]

    zero_list = []
    color_list = [[x, y]]

    while q:
        x, y = q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if find_block_group_con(nx, ny, visited_0, color, game_board):
                if game_board[nx][ny] == 0:
                    zero_list.append([nx, ny])

                else:
                    color_list.append([nx, ny])
                    visited[nx][ny] = True

                q.append([nx, ny])
                visited_0[nx][ny] = True

    if len(color_list) + len(zero_list) == 1:
        return [], []

    color_list.sort(key=lambda x: (x[0], x[1]))
    return color_list, zero_list


def find_block_group_con(nx, ny, visited, color, game_board):
    """ find_block_group 의 조건 함수 """
    if 0 > nx or nx >= N:
        return False
    if 0 > ny or ny >= N:
        return False
    if visited[nx][ny]:
        return False
    if game_board[nx][ny] == 0:
        return True
    if color != game_board[nx][ny]:
        return False
    return True


def sep_block_group(game_board):
    """ 블록 그룹을 나눠주는 함수 """
    visited = visited_init()

    delete_color_list = []
    delete_zero_list = []

    for x in range(N):
        for y in range(N):
            if game_board[x][y] == -1:
                continue

            if game_board[x][y] == -2:
                continue

            if game_board[x][y] == 0:
                continue

            if not visited[x][y]:
                color_list, zero_list = find_block_group(x, y, visited, game_board)
                # print(f"color_list : {color_list}", f"zero_list : {zero_list}")
                if color_list:
                    delete_color_list, delete_zero_list = \
                        find_delete_block_group(color_list, zero_list, delete_color_list, delete_zero_list)

    # print(f"delete_color_list : {delete_color_list}", f"delete_zero_list : {delete_zero_list}")

    return delete_color_list + delete_zero_list


def find_delete_block_group(color_list, zero_list, delete_color_list, delete_zero_list):
    """ 삭제할 블록 그룹을 찾아주는 함수 """
    # 가독성이 엄청 떨어지네;; 좀 더 좋은 방법이 있는지 생각하기
    if len(color_list) + len(zero_list) > len(delete_color_list) + len(delete_zero_list):
        return color_list, zero_list
    elif len(color_list) + len(zero_list) < len(delete_color_list) + len(delete_zero_list):
        return delete_color_list, delete_zero_list

    if len(zero_list) > len(delete_zero_list):
        return color_list, zero_list
    elif len(zero_list) < len(delete_zero_list):
        return delete_color_list, delete_zero_list

    if color_list[0][0] > delete_color_list[0][0]:
        return color_list, zero_list
    elif color_list[0][0] < delete_color_list[0][0]:
        return delete_color_list, delete_zero_list

    if color_list[0][1] > delete_color_list[0][1]:
        return color_list, zero_list

    return delete_color_list, delete_zero_list


def delete_block_group(game_board):  # 이거 임
    """ 블록을 삭제하는 함수 """
    delete_list = sep_block_group(game_board)

    if len(delete_list) == 0:
        return 0

    for x, y in delete_list:
        game_board[x][y] = -2

    return len(delete_list) ** 2


def gravity_block(game_board):
    """ 중력 함수 """
    temp = []

    for y in range(N):
        stack_list = []
        result_list = []
        for x in range(N - 1, -1, -1):
            if game_board[x][y] == -2:
                stack_list.append(-2)
                continue

            if game_board[x][y] == -1:
                result_list.extend(stack_list)
                stack_list = []
                result_list.append(-1)
                continue

            result_list.append(game_board[x][y])
        result_list += stack_list
        temp.append(result_list)

    temp = cycle(temp)

    return temp


def cycle(temp_list):
    """ 90도 돌려주는 함수 """
    temp = []
    for x in temp_list:
        temp.append(reversed(x))

    zip_list = list(zip(*temp))

    for x in range(len(zip_list)):
        temp[x] = list(zip_list[x])

    return temp


def main(game_board):
    """ 함수를 실행 시킬 함수 """
    score = 0

    while True:
        temp = delete_block_group(game_board)

        if temp == 0:
            return score

        score += temp

        game_board = gravity_block(game_board)
        game_board = cycle(game_board)
        game_board = gravity_block(game_board)


print(main(board))

# 해줄 것 -> 기준 블록 잡아주기
# 로직으로 풀어버려서 내 로직을 까먹었네;; 이거 하려면 다 지우고 다시 해야함
# 핵심 로직
# 중력은 스택으로 하기, 회전은 zip으로 하기 그 외는 알아서 해!
# -2는 스택에 넣기, 만약 -1이 나오면 스택에 있는 -2 다 빼고 그 위에 -1 놓기

"""
문제 정리
    나를 굉장히 화나게 하는 문제
    당분간 구현 안할 것
    이걸 쓰는 중에도 정말 화남
    코드는 가독성 높이기
    zip을 잘 활용하면 굉장히 쉽게 풀이 가능
"""
