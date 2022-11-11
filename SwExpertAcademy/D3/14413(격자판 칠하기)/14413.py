"""
    문제 이름 : 격자판 칠하기
    ----------------------------------------------
    <문제 설명>
    격자판을 검은색(#) 또는 흰색(.)으로 칠할 계획이다.
    만약에 격자가 "?"면 어느 색으로 든지 색칠이 가능하다.
    인접한 두 칸의 색이 항상 다르게 할 수 있는지 판단해라.
"""


def check(arr):
    """ 색을 칠할 수 있는지 없는지 확인해주는 함수 """
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(R):
        for c in range(C):
            for z in range(4):
                nr = r + dr[z]
                nc = c + dc[z]
                if 0 > nr or nr >= R:
                    continue
                if 0 > nc or nc >= C:
                    continue

                if arr[r][c] == "#":
                    if arr[nr][nc] == "#":
                        return "impossible"
                    continue

                if arr[r][c] == ".":
                    if arr[nr][nc] == ".":
                        return "impossible"
                    continue

                if arr[nr][nc] == "?":
                    continue

                if arr[r][c] == "?":
                    if arr[nr][nc] == "#":
                        arr[r][c] = "."
                    if arr[nr][nc] == ".":
                        arr[r][c] = "#"

    return "possible"


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        R, C = map(int, input().split())
        board = [list(input()) for _ in range(R)]
        print(f"#{i} {check(board)}")
        # print(*board, sep="\n")
        # print()
