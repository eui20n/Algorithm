"""
    문제 이름 : 1차원 정원
    ----------------------------------------------
    <문제 설명>
    정원의 모든 칸에 꽃이 있다. 이 꽃에 물을 주기 위해서 자동 분무기를 설치할 것이다.
    분무기의 범위는 [위치 - D, 위치 + D]일때, 모든 꽃에 물을 주기위한 최소한의 분무기의 수를 구해라
"""


def sprayer_min():
    """ 최소한의 분무기의 수를 출력해주는 함수 """
    range_sprayer = D * 2 + 1

    if N <= range_sprayer:
        return 1
    elif N % range_sprayer == 0:
        return N // range_sprayer
    return N // range_sprayer + 1


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        N, D = map(int, input().split())
        result = sprayer_min()
        print(f"#{i} {result}")
