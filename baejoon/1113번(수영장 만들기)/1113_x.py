"""
    문제 이름 : 수영장 만들기
    URL : https://www.acmicpc.net/problem/1113
    ----------------------------------------------
    <문제 설명>
    그래프가 주어질때 물이 고일 수 있는지, 그리고 고인다면 얼마나 고이는지 출력하면 된다.
    1 <= 물의 높이 <= 9 이다
    무조건 물이 고일 수 있다고 생각할 것 -> 물이 고일 수 없을시 출력값이 없음
"""
from collections import deque

R, C = map(int, input().split())
graph = [list(map(int, input())) for _ in range(C)]

def init_visited():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False]*C for _ in range(R)]
    visited = side_change(visited)
    return visited

def side_change(arr):
    """ 가장 자리를 True로 바꿔주는 함수 """
    for x in range(R):
        arr[x][0] = True
        arr[x][C-1] = True

    for y in range(C):
        arr[0][y] = True
        arr[R-1][y] = True

    return arr


# 생각이 난 풀이
# 4방향을 조사해서 차이가 가장 큰 쪽으로 감, 이걸 옆으로 계속 반복하면 됨, 이렇게 차이가 구해진 것은 TRUE로 해서 다시는 안해지게 하면 됨
# 반례 있나 생각해보기