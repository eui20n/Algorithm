"""
    문제 이름 : 놀이 공원
    URL : https://www.acmicpc.net/problem/1561
    ----------------------------------------------
    <문제 설명>
    N명의 아이들이 M 종류의 1인승 놀이기구를 기다리고 있다.
    모든 놀이기구는 운행시간이 정해져 있어서, 운행 시간이 지나면 탑승하고 있던 아이는 내리게 됨
    놀이 기구가 비어있으면 현재 줄에서 가장 앞에 있는 아이가 놀이 기구를 탑승함
    만약 여러 놀이기구가 비어있으면 번호가 저 작은 놀이기구를 탑승함
    놀이기구가 모두 비어 있는 상태에서 첫 번째 아이가 놀이기구에 탑승하다고 할 때, 줄의 마지막 아이가 타게 되는 놀이기구의 번호를 구해라
    놀이기구의 번호는 1부터 간다
"""
N, M = map(int, input().split())
play_time = list(map(int, input().split()))


def binary_search(num):
    """ 이분탐색을 해주는 함수 """
    start = 1
    end = N

    while True:
        mid = (start + end) // 2

        # 현재 위치의 어린이가 놀이기구에 탔나요?
        if num & (1 << mid):
            start = mid + 1
        else:
            end = mid


def main():
    """ 함수를 실행시켜줄 함수 """
    # 비트마스킹으로 접근할 것인데, 1번부터 갈거라서 1로 해줌
    children = 1
    binary_search(children)

