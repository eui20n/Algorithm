"""
    문제 이름 : 불 끄기
    URL : https://www.acmicpc.net/problem/14939
    ----------------------------------------------
    <문제 설명>
    10x10의 전구가 있다. 서로 인접한 전구에 대해서 스위치를 누르면 상태가 바뀐다(on -> off, off -> on)
    이 때 모든 전구를 끄기 위해 누르는 스위치의 개수 중 최소값을 구해라

    자기 위치 포함, 위 아래 양옆이 바뀜 -> 그렇다면 중간에 있는건 누를 필요가 없음
"""

bulb = [list(map(str, input())) for _ in range(10)]

def change_bulb():
    """ 보기 편하게 바꾸는 함수, #은 꺼진 것 0, O은 켜진 것 1"""
    for x in range(10):
        for y in range(10):
            if bulb[x][y] == '#':
                bulb[x][y] = 0

            else:
                bulb[x][y] = 1

# 어려우네