"""
    문제 이름 : 다각형의 면적
    URL : https://www.acmicpc.net/problem/2166
    ----------------------------------------------
    <문제 설명>
    2차원 평면상의 다각형의 좌표가 주어질 때, 면적을 구하면 된다
"""
N = int(input())
x_n, y_n = [], []
for _ in range(N):
    x, y = map(int, input().split())
    x_n.append(x)
    y_n.append(y)

x_n.append(x_n[0])
y_n.append(y_n[0])


def cal_size():
    """ 면적을 구해주는 함수 """
    xy = 0
    yx = 0
    for idx in range(len(x_n) - 1):
        xy += x_n[idx] * y_n[idx + 1]
        yx += y_n[idx] * x_n[idx + 1]

    result = abs(xy - yx) / 2

    return round(result, 1)


print(cal_size())


"""
        핵심정리
    1. 그냥 공식이 있음 -> 인터넷에 검색하면 나옴
"""