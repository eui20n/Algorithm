"""
    문제 이름 : 낮잠 시간
    URL : https://www.acmicpc.net/problem/1988
    ----------------------------------------------
    <문제 설명>
    낮잠 시간을 N개의 구간으로 나누어서 B개의 구간동안 잠을 자려고함
    B개의 구간은 연속일 필요는 없음
    이 때, 얻을 수 있는 피로 회복량이 정해져 있는데 이 값의 최대값을 출력해라

    여기서 구간의 처음은 준비 기간이라서 이 때는 피로 회복을 못함함
"""


def dp():
    """ 함수를 실행시켜 주는 함수 """
    dp_table = [0] * (N + 1)

    for idx in range(B, N + 1):
        temp_sum = 0
        for pre_idx in range(idx, idx - B + 1, -1):
            temp_sum += fatigue_recover[pre_idx]

        dp_table[idx] = max(dp_table[idx - 1], temp_sum)

    print(dp_table[N])


if __name__ == "__main__":
    N, B = map(int, input().split())
    fatigue_recover = [0]
    for _ in range(N):
        n = int(input())
        fatigue_recover.append(n)

    dp()
