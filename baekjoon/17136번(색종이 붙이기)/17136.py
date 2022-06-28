"""
    문제 이름 : 색종이 붙이기
    URL : https://www.acmicpc.net/problem/17136
    ----------------------------------------------
    <문제 설명>
    1 x 1, 2 x 2, 3 x 3, 4 x 4, 5 x 5 크기의 종이가 5개씩 있다
    이 종이를 10 x 10에 지정한 곳에 붙이려고 할때 필요한 종이의 최소 값은 몇인가?
    만약 종이를 붙일 수 없으면 -1을 출력해라
"""

paper = [list(map(int, input().split())) for _ in range(10)]
result = float('inf')


def paste_paper(x, y, cnt_1, cnt_2, cnt_3, cnt_4, cnt_5, arr):
    """ 종이를 붙이는 함수 """
    global result

    cnt = [cnt_1, cnt_2, cnt_3, cnt_4, cnt_5]
    if result < sum(cnt):
        return

    if x == 10 and y == 0:
        if result > sum(cnt):
            result = sum(cnt)
        return

    if x >= 10 or y >= 10:
        return

    if arr[x][y] == 0:
        if y == 9:
            paste_paper(x + 1, 0, cnt[0], cnt[1], cnt[2], cnt[3], cnt[4], arr)
        else:
            paste_paper(x, y + 1, cnt[0], cnt[1], cnt[2], cnt[3], cnt[4], arr)

    elif arr[x][y] == 1:
        for d in [1, 2, 3, 4, 5]:
            temp = [temp_list[:] for temp_list in arr]
            if d_by_d(x, y, d, temp):
                if cnt[d - 1] < 5:
                    cnt[d - 1] += 1
                    if y == 9:
                        paste_paper(x + 1, 0, cnt[0], cnt[1], cnt[2], cnt[3], cnt[4], temp)
                    else:
                        paste_paper(x, y + 1, cnt[0], cnt[1], cnt[2], cnt[3], cnt[4], temp)
                    cnt[d - 1] -= 1

            else:
                return


def d_by_d(x, y, d, arr):
    """ 현재 위치를 기준으로 d x d를 붙일 수 있는지 확인해 주는 함수 """
    for idx_x in range(x, x + d):
        for idx_y in range(y, y + d):
            if 0 > idx_x or idx_x >= 10:
                return False
            if 0 > idx_y or idx_y >= 10:
                return False
            if not arr[idx_x][idx_y]:
                return False

            arr[idx_x][idx_y] = 0

    return True


def main():
    """ 함수를 실행 시켜줄 함수 """
    paste_paper(0, 0, 0, 0, 0, 0, 0, paper)
    if result == float('inf'):
        print(-1)
    else:
        print(result)


main()

"""
        소요 시간
    오랜만에 하루가 넘은 문제 -> 소요 시간을 측정하는게 무의미
    
        핵심 정리
    1. 백트래킹으로 들어갈 때, 처음부터가 아닌 들어가 그 위치에서 시작해야지 시작이 안 넘음
    2. 만약 현재 위치에서 2 x 2가 안되면 그 것보다 더 큰 3 x 3, 4 x 4, 5 x 5도 다 안되는 것
    
        느낀점
    1. 나 백트래킹 많이 못하는 듯...ㅠ
    2. 재귀에 대해서 좀 더 이해가 필요할 듯 -> 조만간 백트래킹만 할 것
"""