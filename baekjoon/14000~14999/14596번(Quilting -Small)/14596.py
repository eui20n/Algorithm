"""
    문제 이름 : Quilting (Small)
    URL : https://www.acmicpc.net/problem/14596
    ----------------------------------------------
    <문제 설명>
    이미지 퀄팅(Quilting)이란, 하나의 패턴 이미지를 여러 개 이어붙여서 큰 이미지를 만들어내는 것을 말함
    이를 자연스럽게 하기 위해서 아래의 방법을 이용하여 아래의 방법을 이용한다
    1. 이어붙일 두 이미지를 B1, B2라고 하자
    2. 두 이미지의 경계를 조금 포갠다. 포갠 영역의 너비는 최소 2픽셀이다
    3. 포개어진 영역에서 B2와 B1 이미지의 차이가 최소가 되도록 경계선을 결정한다. 그리고 경계선과 그 오른쪽 부분을 B1 이미지에 B2이미지를
       덮어써서 새로운 이미지를 생성한다.
      3-1. 경계선은 포개진 영역의 한 행마다 하나의 픽셀을 선택하여 생성한다.
      3-2. 경계선의 각 행에 선택된 픽셀은 바로 위 혹은 아래 행에서 선택된 픽셀과 두 칸 이상 떨어질 수 없다.
           즉, 한 경계선 픽셀은 자신의 바로 아래 혹은 위의 행 경계선 픽셀과 좌우로 +1, 0, 1칸 차이가 나는 것만 허용한다.
      3-3. 각 행은 경계선으로 선택된 픽셀을 기준으로 그 왼쪽은 B1 이미지의 픽셀을 그대로 사용하고,
           픽셀과 이후 오른쪽 픽셀들은 B2 이미지의 픽셀로 덮어쓰게 된다.

    이러한 경계는 많아서 가장 자연스럽게 두 이미지를 붙일 수 있는 경계선을 선택해야한다.
    이 기준은 각 픽셀 위치에서의 B1 이미지의 픽셀과 B2 이미지의 픽셀의 색상 값의 차를 제곱하여 모두 더한 값이다.
    가장 자연스러운 것은 이 값이 낮다
    이 때, 최소의 부자연스러운 정도를 구해라
"""


def show_arr(arr):
    """ 배열을 보여주는 함수 """
    print(*arr, sep='\n')


def change(arr_1, arr_2):
    """ 기존의 배열을 바꿔주는 함수 """
    new_arr = [[0 for _ in range(C)] for _ in range(R)]

    for x in range(R):
        for y in range(C):
            value = abs(arr_1[x][y] - arr_2[x][y])
            new_arr[x][y] = value

    return new_arr


def dp(dp_table, arr):
    """ dp를 해주는 함수 """
    direction = [-1, 0, 1]

    for y in range(C):
        dp_table[0][y] = arr[0][y] ** 2

    for x in range(1, R):
        for y in range(C):
            for d in direction:
                new_dir = y + d
                if 0 <= new_dir < C:
                    dp_table[x][y] = min(dp_table[x][y], dp_table[x - 1][new_dir])

            dp_table[x][y] += arr[x][y] ** 2


def main():
    """ main 함수 """
    new_arr = change(board_1, board_2)
    dp_table = [[float('inf') for _ in range(C)] for _ in range(R)]
    dp(dp_table, new_arr)
    result = min(dp_table[R - 1])
    return result


if __name__ == "__main__":
    R, C = map(int, input().split())
    board_1 = []
    board_2 = []

    for _ in range(R):
        temp_arr = list(map(int, input().split()))
        board_1.append(temp_arr)

    for _ in range(R):
        temp_arr = list(map(int, input().split()))
        board_2.append(temp_arr)

    print(main())
