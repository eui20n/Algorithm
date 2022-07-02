"""
    문제 이름 : 게임
    URL : https://www.acmicpc.net/problem/1103
    ----------------------------------------------
    <문제 설명>
    가장 왼쪽 위에서 시작해서 해당 칸에 있는 숫자만큼 동서남북으로 간다
    위 과정을 아래의 규칙으로 반복한다
    1. 동전이 구멍에 빠지면 끝
    2. 동전이 범위를 벗어나면 끝
    위 규칙을 지키면서 반복할 때 최대로 몇번 반복할 수 있는지 구해라
    단, 무한히 반복이 된다면 -1을 출력해라
"""
R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]
dp_table = [[0] * C for _ in range(R)]
check_inf = False


def visited_init():
    """ 방문처리 리스트를 만들어 주는 함수 """
    visited = [[False] * C for _ in range(R)]
    return visited


def play_game(x, y, visited):
    """ 게임을 해주는 함수 """
    global check_inf

    if check_inf:
        return 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for z in range(4):
        nx = x + dx[z] * int(board[x][y])
        ny = y + dy[z] * int(board[x][y])
        if 0 > nx or nx >= R or 0 > ny or ny >= C or board[nx][ny] == 'H':
            continue

        if visited[nx][ny]:
            check_inf = True
            return 0

        if dp_table[nx][ny] != 0:
            dp_table[x][y] = max(dp_table[nx][ny] + 1, dp_table[x][y])
            continue

        visited[nx][ny] = True
        dp_table[x][y] = max(play_game(nx, ny, visited), dp_table[x][y])
        visited[nx][ny] = False

    dp_table[x][y] = max(dp_table[x][y], 1)
    return dp_table[x][y] + 1


def main():
    """ 함수를 실행 시켜줄 함수 """
    visited = visited_init()
    visited[0][0] = True
    play_game(0, 0, visited)

    if check_inf:
        return "-1"
    else:
        return dp_table[0][0]


print(main())


"""
        핵심 정리
    1. 무한으로 들어가는 경우만 잘 체크하면 된다
    2. 무한으로 들어가는 경우는, 한번 방문한 곳이면 다시 방문하면 무한히 돈다는 것임 -> 근데 방문처리를 할 때 재귀로 나오면 False로 바꿔줘야함
"""


