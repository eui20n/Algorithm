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
result_set.add(float('inf'))


def find_paste():
    """ 붙힐 곳을 찾아 주는 함수 """
    temp = set()
    for x in range(10):
        for y in range(10):
            if paper[x][y] == 1:
                temp.add((x, y))

    return temp


def paper_paste(cnt_1, cnt_2, cnt_3, cnt_4, cnt_5, result, paste):
    """ 종이를 붙여주는 함수 """
    if result >= min(result_set):
        return

    if len(paste) == 0:
        result_set.add(result)
        return

    cnt = [cnt_1, cnt_2, cnt_3, cnt_4, cnt_5]

    for x, y in paste:
        for d in [1, 2, 3, 4, 5]:
            temp = {x[:] for x in paste}
            if cnt[d - 1] < 5 and d_dy_d(x, y, d, temp):
                if d == 1:
                    paper_paste(cnt_1 + 1, cnt_2, cnt_3, cnt_4, cnt_5, result + 1, temp)
                elif d == 2:
                    paper_paste(cnt_1, cnt_2 + 1, cnt_3, cnt_4, cnt_5, result + 1, temp)
                elif d == 3:
                    paper_paste(cnt_1, cnt_2, cnt_3 + 1, cnt_4, cnt_5, result + 1, temp)
                elif d == 4:
                    paper_paste(cnt_1, cnt_2, cnt_3, cnt_4 + 1, cnt_5, result + 1, temp)
                elif d == 5:
                    paper_paste(cnt_1, cnt_2, cnt_3, cnt_4, cnt_5 + 1, result + 1, temp)


def d_dy_d(x, y, d, paste):
    """ 현재 위치를 기준으로 d x d를 붙일 수 있는지 확인해 주는 함수 """
    for idx_x in range(x, x + d):
        for idx_y in range(y, y + d):
            if (idx_x, idx_y) not in paste:
                return False
            paste.remove((idx_x, idx_y))
    return True


def main():
    """ 함수를 실행 시켜줄 함수 """
    paste = find_paste()
    paper_paste(0, 0, 0, 0, 0, 0, paste)
    if len(result_set) == 0:
        return -1
    return result_set


print(main())

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

# 혹시 무한 루프가 있을 수도 있으니 다음에 다시 풀때, 좀 더 꼼꼼히 보기