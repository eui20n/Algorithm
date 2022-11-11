"""
    문제 이름 : 숫자가 같은 배수
    ----------------------------------------------
    <문제 설명>
    자연수 N이 있다. N은 10진법 표기에서 나타나는 숫자들을 재배열하여 N보다 큰 N의 배수를 만들 수 있는지 판단해라
"""


def check(num):
    num_list = list(str(num))
    num_length = len(num_list)

    num_cnt = [0 for _ in range(10)]

    for idx in range(num_length):
        new_idx = int(num_list[idx])
        num_cnt[new_idx] += 1

    k = 2

    while True:
        new_num = num * k
        new_num_list = list(str(new_num))

        new_num_cnt = [0 for _ in range(10)]

        for idx in range(len(new_num_list)):
            new_idx = int(new_num_list[idx])
            new_num_cnt[new_idx] += 1

        k += 1

        if new_num_cnt == num_cnt:
            return "possible"
        if num_length < len(new_num_list):
            return "impossible"


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        result = check(N)
        print(f"#{i} {result}")


"""
        문제 풀이
    배수의 수의 배열에 있는 숫자들이 원래에 있던 숫자의 배열에 있는지 확인하면 됨
    여기서 그냥 확인하면 같은 수 2개 이상(example 1122)에 대해서 처리를 할 수 없다고 판단하여 개수를 세고 개수로 판단함
"""