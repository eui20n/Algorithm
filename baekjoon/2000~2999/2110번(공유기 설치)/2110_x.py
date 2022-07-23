"""
    문제 이름 : 공유기 설치
    URL : https://www.acmicpc.net/problem/2110
    ----------------------------------------------
    <문제 설명>
    C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 구해라
"""
house_num, ip_time = map(int, input().split())
house = []
for _ in range(house_num):
    temp_input = int(input())
    house.append(temp_input)
house.sort()


def binary_search(arr, start, end):
    """ 이분 탐색을 해주는 함수 """
    if start > end:
        return end

    mid = (start + end) // 2
    start_mid = arr[mid] - house[0]
    mid_end = arr[end] - arr[mid]

    if start_mid <= mid_end:
        return binary_search(arr, mid + 1, end)
    else:
        return binary_search(arr, start, mid - 1)


def main():
    """ 함수를 실행시켜주는 함수 """
    if ip_time > 2:
        new_arr = house[1:len(house) - ip_time + 2]
        result = binary_search(new_arr, 0, len(new_arr) - 1)
        return new_arr[result] - house[0]

    else:
        return house[len(house) - 1] - house[0]


print(main())
