"""
    문제 이름 : 정사각형 판정
    ----------------------------------------------
    <문제 설명>
    N x N 에 비어 있거나(".") 막혀("#") 있다. 이 때, 막혀있는 칸들이 하나의 정사각형을 이루는지 출력해라
    이 때, 1개의 정사각형인지를 확인하면 됨
"""


def check():
    """ 한개의 정사각형인지 확인해주는 함수 """
    cnt = 0

    for r in range(N):
        for c in range(N):
            if board[r][c] == "#":
                check_square(r, c)
                cnt += 1

    if cnt == 1:
        return "yes"
    return "no"


def check_square(r, c):
    loc = []
    length = 0

    for nc in range(c, N):
        if board[r][nc] == "#":
            length += 1

    for nr in range(r, r + length):
        for nc in range(c, c + length):
            if 0 > nr or nr >= N:
                return False
            if 0 > nc or nc >= N:
                return False
            if board[nr][nc] == ".":
                return False
            loc.append([nr, nc])

    for nr, nc in loc:
        board[nr][nc] = "."

    return True


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        board = [list(input()) for _ in range(N)]
        result = check()
        # print(*board, sep="\n")
        print(f"#{i} {result}")
