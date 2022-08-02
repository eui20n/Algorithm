"""
            유클리드 호제법
    2개의 자연수 또는 정식의 최대공약수를 구하는 알고리즘이다.
    이 알고리즘의 핵심은 다음과 같다.
    두 자연수 a, b가 있다고 하자. (a > b)
    이 두 자연수 a, b의 최대공약수는 a/b의 나머지 r과 b의 최대공약수와 같다.
    이 성질을 무한히 반복하여 나머지가 0이 될 떄, 나누는 수가 a와 b의 최대공약수가 된다
"""


# 재귀를 이용한 방법
def gcd(m, n):
    # 무조건 m이 더 큰수가 되게 해줌
    if m < n:
        m, n = n, m

    # n을 나눈 수는 m이기 때문에 m을 리턴함
    if n == 0:
        return m

    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


# while문을 활용하는 방법
def gcd_while(m, n):
    while n != 0:
        # t는 나머지이고 이것으로 계속 n값을 바꿈
        t = m % n
        m, n = n, t
    return abs(m)


if __name__ == "__main__":
    m, n = 100, 10
    print(gcd(m, n))
    print(gcd_while(m, n))

