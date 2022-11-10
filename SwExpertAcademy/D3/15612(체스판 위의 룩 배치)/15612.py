"""
    문제 이름 : 체스판 위의 룩 배치
    ----------------------------------------------
    <문제 설명>
    8 * 8 크기의 체스판 위의 몇 개의 칸에 룩이 있다. 각 칸에는 최대 1개의 룩을 놓을 수 있다 => 룩의 개수는 0 ~ 64개
    이때, 현재 체스판의 배치가 다음 조건을 모두 만족하는지 판별해라
    1. 정확히 8개의 룩이 있어야 한다.
    2. 모든 룩은 서로 공격할 수 없어야 한다. 즉, 서로 다른 두 룩은 같은 열에 있거나 행에 있으면 안 된다.
"""


def check(arr):
    place_column_in_rock = set()
    for r in range(8):
        rook = 0
        for c in range(8):
            if arr[r][c] == "O":
                if c in place_column_in_rock:
                    return "no"

                place_column_in_rock.add(c)
                rook += 1

            if rook >= 2:
                return "no"

    if len(place_column_in_rock) != 8:
        return "no"
    return "yes"


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        board = [list(input()) for _ in range(8)]
        result = check(board)
        print(f"#{i} {result}")
