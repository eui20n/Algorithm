"""
파이썬 힙 자료 구조 구현
"""
def build_heap(arr: list, n: int) -> list:
    """
    heap 자료 구조로 만들어 주는 함수
    :param arr: 리스트가 들어가는 파라미터
    :param n: arr의 길이
    :return: 반환값은 리스트로 나와야함
    """
    for i in range(n//2,0,-1):
        heapify(arr,i,n)

def heapify(arr: list,k: int,n: int) -> None:
    """
    재귀적으로 호출해서 힙을 만들어 주는 함수
    :param arr: 힙 으로 바꾸고 싶은 리스트
    :param k: arr의 인덱스 번호 중 하나
    :param n: arr의 길이
    :return: 반환값은 없음
    """
    left = 2*k
    right = 2*k+1

    if right <= n:
        if arr[left] < arr[right]:
            smaller = left
        else:
            smaller = right

    elif left <= n:
        smaller = left
    else:
        return

    if arr[smaller] < arr[k]:
        arr[k],arr[smaller] = arr[smaller], arr[k]
        heapify(arr,smaller,n)

def heap_sort(arr: list, n: int) -> None:
    """
    힙 정렬을 해주는 함수
    :param arr: 리스트
    :param n: arr의 길이
    :return: 반환 값은 없음
    """
    build_heap(arr, n)
    for i in range(n, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(arr, 1, i-1)

if __name__ == '__main__':
    arr = [7,9,4,8,6,3]
    arr = [0] + arr
    print(arr)
    build_heap(arr,len(arr)-1)
    print(arr)
    heap_sort(arr,len(arr)-1)
    print(arr)