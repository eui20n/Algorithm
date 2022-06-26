"""
    문제 이름 : 색종이 붙이기
    URL : https://www.acmicpc.net/problem/17136
    ----------------------------------------------
    <문제 설명>
    1 x 1, 2 x 2, 3 x 3, 4 x 4, 5 x 5 크기의 종이가 5개씩 있다
    이 종이를 10 x 10에 지정한 곳에 붙이려고 할때 필요한 종이의 최소 값은 몇인가?
    만약 종이를 붙일 수 없으면 -1을 출력해라
"""
from copy import deepcopy

paper = [list(map(int, input().split())) for _ in range(10)]
result_set = set()


def paper_paste(cnt, result, board):
    """ 종이를 붙여줄 함수 """

    for x in range(10):
        for y in range(10):
            if board[x][y] == 0:
                continue

            for d in [1, 2, 3, 4, 5]:
                temp = [x[:] for x in board]
                if d_by_d(x, y, d, temp) and cnt[d - 1] < 5:
                    print(cnt)
                    print(*temp, sep='\n')
                    print()
                    cnt[d - 1] += 1
                    paper_paste(cnt, result + 1, temp)

    for x in range(10):
        for y in range(10):
            if board[x][y] == 1:
                return

    result_set.add(result)


def d_by_d(x, y, d, board):
    """ 현재 위치 기준으로 d x d 을 봐주는 함수 """
    for idx_x in range(x, x + d):
        for idx_y in range(y, y + d):
            if 0 > idx_x or idx_x >= 10:
                return False
            if 0 > idx_y or idx_y >= 10:
                return False
            if board[idx_x][idx_y] == 0:
                return False

    for idx_x in range(x, x + d):
        for idx_y in range(y, y + d):
            board[idx_x][idx_y] = 0

    return True


def main():
    """ 함수를 실행 시켜줄 함수 """
    paper_paste([0, 0, 0, 0, 0], 0, paper)
    if len(result_set) == 0:
        return -1
    return min(result_set)


print(main())
print(result_set)
# d_by_d(0, 0, 5, paper)
# print(*paper, sep='\n')

# 그냥 재귀 한번 돌리면 끝날 듯
# 고민할 것 -> 각각의 종이를 어떻게 구현할지 ==> 도저히 생각이 안나면 그냥 노가다로 구현해도 됨
# 무조건 -1이 나온다고 종료하면 안됨
# 함수의 인자는 각각의 종이가 몇번 사용됫는지, 현재 위치, 종이 배열 => 현재위치 빼기

# 0 일때 1
# 1 일때 2
# 2 일때 3
# 3 일때 4
# 4 일때 5
# 5이면 하면 안됨
