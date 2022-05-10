"""
    문제 이름 : 불 끄기
    URL : https://www.acmicpc.net/problem/14939
    ----------------------------------------------
    <문제 설명>
    10x10의 전구가 있다. 서로 인접한 전구에 대해서 스위치를 누르면 상태가 바뀐다(on -> off, off -> on)
    이 때 모든 전구를 끄기 위해 누르는 스위치의 개수 중 최소값을 구해라

    상태는 on,off 두개이다 -> 비트단위로 생각하기 -> 모두 끄고 싶은거니까 모든 값이 0이 되면 됨됨
    불가능하면 -1을 출력하면 됨 -> for문이 끝나면 -1 출력
"""

bulb = [list(map(str, input())) for _ in range(10)]

def change_bulb(bulb):
    """
    불이 켜진 상태를 0과 1로 표현, 0 -> 꺼진 상태, 1 -> 켜진 상태
    이진수로 표현할 것
    """
    temp = [0]*10

    for x in range(10):
        for y in range(10):
            if bulb[x][y] == 'O':
                temp[y] |= 1 << x

    return temp

def off_light(arr):
    """ 불을 꺼주는 함수 """
    for y in range(10):
        for x in range(10):
            if arr[y] & (1 << x):
                pass


# 내 수준의 문제가 아닌듯;;



# print(change_bulb(bulb))

# 앞에서 부터 숫자가 카운트 됨
# 목표는 한줄씩 0을 만들기 -> 한번에 모든 칸을 0으로 만들 필요 없음
## 만약에 그 칸을 1을 지우지 못할 경우 그냥 넘기기
### 최종적으로 모든 리스트의 합이 0인지 아닌지 확인하기
