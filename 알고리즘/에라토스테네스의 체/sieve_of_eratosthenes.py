"""
            에라토스테네스의 체
    소수 판별 알고리즘으로 많은 수의 소수를 판별할 때 아주 적은 시간으로 구할 수 있다.
    특히 넓은 범위에서 소수를 구하고 싶을 때 사용하면 좋다. => 1 ~ 1000000 사이의 모든 소수 구하기 등등

    시간 복잡도 : O(N^(1/2))
"""


# 소수를 판별해주는 함수
def check_prime(num):
    # 2부터 시작을 하기 때문에 제일 처음은 True로 한다.
    # 또한 인덱스 번호랑 수를 같게하기 위해서 제일 처음에 True를 또 더해준다.
    visited = [True] * (num + 1)

    root_num = int(num ** (1/2))

    for idx in range(2, root_num + 1):
        if not visited[idx]:
            continue

        # 여기서 2 * idx인 이유는 자기 자신은 소수이기 때문이다.
        for not_prime_idx in range(2 * idx, num + 1, idx):
            visited[not_prime_idx] = False

    prime_num = []
    for idx in range(2, len(visited)):
        if visited[idx]:
            prime_num.append(idx)

    print(*prime_num, sep=" ")


if __name__ == "__main__":
    # 1 ~ 100000 사이의 모든 소수를 알고 싶음 => n은 범위의 끝값
    n = 100
    check_prime(n)

