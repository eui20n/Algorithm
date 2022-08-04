"""
    문제 이름 : 기타 레슨
    URL : https://www.acmicpc.net/problem/2343
    ----------------------------------------------
    <문제 설명>
    i번 강의부터 j번 강의까지 녹화하고 블루레이에 담으려고 할 때, 블루레이의 수를 최대한 줄이고 싶다.
    이 때, 블루레이 1개의 용량을 몇으로 하면 되는지 출력해라 -> 모든 블루레이의 용량은 같음
"""


def binary_search(start, end):
    """ 이분탐색을 해주는 함수 """
    while True:
        if start >= end:
            break

        mid = (start + end) // 2
        check = check_record(mid)

        if check:
            start = mid + 1
        else:
            end = mid

    return end


def check_record(num):
    """ 녹화 가능한지 알려주는 함수 """
    cnt = 0
    temp = 0
    for x in lesson:
        if x > num:
            return True

        if temp + x > num:
            temp = x
            cnt += 1
            continue

        temp += x

    if cnt >= blue_cnt:
        return True
    else:
        return False


def main():
    """ 함수를 실행시켜주는 함수 """
    return binary_search(1, sum(lesson))


if __name__ == "__main__":
    n, blue_cnt = map(int, input().split())
    lesson = list(map(int, input().split()))
    print(main())


"""
    이분 탐색 + 파라메틱 서치 문제
"""