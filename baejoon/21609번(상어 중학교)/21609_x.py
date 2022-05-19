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
    visited = [[False] * N for _ in range(N)]  # 만약에 필요 없으면 지울 것

    for x in range(N):
        for y in range(N):
            if board[x][y] == 'x':
                visited[x][y] = True

    return visited


def find_block_group(x, y, visited):
    """ 블록 그룹을 찾아 주는 함수 """
    if board[x][y] == -1:
        return False

    visited[x][y] = True

    # 무지개 색또 포함한 방문 처리 리스트
    visited_0 = visited_init()
    visited_0[x][y] = True

    color = board[x][y]  # 그 구역의 색

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append([x, y])

    result = [[x, y, color]]
    temp_cnt = 0

    while q:
        x, y = q.popleft()

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if find_block_group_con(nx, ny, color, visited_0):
                if board[nx][ny] != 0:
                    visited[nx][ny] = True

                if board[nx][ny] == 0:
                    temp_cnt += 1

                q.append([nx, ny])
                visited_0[nx][ny] = True
                result.append([nx, ny, board[nx][ny]])  # x, y, 그 위치의 색

    if len(result) < 2:
        return False

    # 모두 0인 그룹은 False를 반환해줌
    if sum(list(zip(*result))[2]) == 0:
        return False

    for x in range(len(result)):
        result[x].append(temp_cnt)

    return result


def find_block_group_con(x, y, color, visited):
    """ find_block_group 함수의 조건 함수 """
    if 0 > x or x >= N:
        return False
    if 0 > y or y >= N:
        return False
    if visited[x][y]:
        return False
    if board[x][y] == 0:
        return True
    if board[x][y] != color:
        return False
    return True


def sep_block_group():
    """ 블록 그룹을 나눠 주는 함수 """
    visited = visited_init()

    block_group_list = []

    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                temp = find_block_group(x, y, visited)

                if temp:
                    temp.sort(key=lambda x: (-x[3], -x[2], x[0], x[1]))
                    block_group_list.append(temp)

    return block_group_list


def delete_block_group():
    """ 상어 그룹을 없애는 함수 """
    # 1. 가장 많은 그룹 없애기
    # 2. 1번이 여러개면 무지개 그룹이 제일 많은 것 -> 어디에 담아서 줄지 생각하기
    # 3. 2번도 여러개면 기준 블록 행이 가장 작은 것
    # 4. 3번도 여러개면 기준 블록 열이 가장 작은 것
    # 위 의 규칙에 맞게 없애기
    # 해결

    block_group = sorted(sep_block_group(), key=lambda x: (-len(x)))

    # 삭제할 블록들
    delete_blocks = block_group[0]

    for x in delete_blocks:
        board[x[0]][x[1]] = 'x'

    return len(delete_blocks) ** 2


def gravity_block():
    """ 중력을 담당해 주는 함수 """

    # 이분 탐색으로 내리기
    for y in range(N - 1, -1, -1):
        cnt = N - 1
        for x in range(N - 1, -1, -1):
            if board[x][y] == -1:
                continue

            if board[x][y] == 'x':
                continue






# print("sep", *sep_block_group(), sep = '\n')
# print("delete", *delete_block_group(), sep='\n')

delete_block_group()
print(*board, sep='\n')

# 블록 그룹을 나눌 때 0인 부분은 bfs안돌려도 됨 -> 하지만 그룹 안에는 속해야함
# 검은 색 블록도 bfs 안돌려도 됨, 또한 그룹에 속하게 하면 안됨 -> 즉, bfs 돌리는건 색이 있는 블록임
# 문제에 대한 의문 사항 -> 무지개 색깔 블록은 여러 그룹에 겹치게 있어도 되나?? => 일단 가능하게 짜기
# zip을 활용해서 0만 있는지 없는지 찾기 -> find_block_group에서
