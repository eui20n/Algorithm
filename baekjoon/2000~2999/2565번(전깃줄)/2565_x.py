"""
    문제 이름 : 전깃줄
    URL : https://www.acmicpc.net/problem/2565
    ----------------------------------------------
    <문제 설명>
    교차하는 전깃줄을 없애 교차하지 않게 만들려고 한다.
    이 때, 전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때, 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해
    없애야 하는 전깃줄의 최소 개수를 구해라
"""


def dp(dp_table):
    """ dp 함수 """
    dp_table[1] = 0


def main():
    """ 함수를 실행시켜주는 함수 """
    dp_table = [0 for _ in range(N + 1)]
    dp(dp_table)


if __name__ == "__main__":
    N = int(input())
    power_pole = [[] for _ in range(N)]
    for idx in range(N):
        a, b = map(int, input().split())
        power_pole[idx] += [a, b]
    power_pole.sort()

    main()
    print(power_pole)
