"""
    문제 이름 : 소수 찾기
    URL : https://www.acmicpc.net/problem/1978
    ----------------------------------------------
    <문제 설명>
    주어진 수 중에서 소수의 개수를 출력해라
"""


def check_prime():
    """ 소수를 판별해주는 함수 """
    root_n = int(1000 ** (1/2))
    visited = [True] * 1001

    for idx in range(2, root_n + 1):
        if not visited[idx]:
            continue

        for prime in range(2 * idx, 1001, idx):
            visited[prime] = False

    return visited


def main(arr):
    """ 함수를 실행시켜주는 함수 """
    temp_list = check_prime()
    cnt = 0
    for x in arr:
        if x == 1:
            continue
        if temp_list[x]:
            cnt += 1

    return cnt


if __name__ == "__main__":
    n = int(input())
    num = list(map(int, input().split()))
    print(main(num))

