"""
    문제 이름 : 어항 정리
    URL : https://www.acmicpc.net/problem/23291
    ----------------------------------------------
    <문제 설명>
    연산 순서
    1. 물고기가 가장 작은 어항에 물고기를 한마리 넣는다.
    1-1. 만약 위와 같은 어항이 어려개라면 그 어항들에 물고기를 한 마리 넣는다.
    2. 가장 왼쪽에 있는 어항을 그 어항의 오른쪽에 있는 어항에 쌓는다.
    3. 2개 이상 쌓여있는 어항을 모두 90도 방향 회전 시킨다.
    3-1. 이 과정을 쌓여있는 가장 오른쪽 어항의 바닥에 어항이 있을때 까지 반복한다.
    3-2. 만약에 회전 시켰는데 가장 오른쪽 어항의 바닥에 어항이 없으면 안된다.
    4. 인접한 어항의 물고기의 수를 조절해 주면 된다.
    4-1. 인접한 두 어항의 물고기 수의 차이를 구하고 그 차이를 5로 나눈 몫을 d라고 한다.
    4-2. d가 0보다 크면 물고기 더 많은 쪽에서 적은쪽으로 d마리 만큼 보낸다.
    4-3. 이 과정은 동시에 일어난다.
    5. 그 후 다시 바닥에 일렬로 놓아야 한다.
    5-1. 가장 왼쪽에 있는 어항, 그 중 가장 아래에 있는 어항순서 대로 일렬로 바닥에 놓으면 된다.
    6. 그 후 가운데를 중심으로 왼쪽에 있는 어항 N/2개를 180도 회전시켜 쌓는다.
    6-1. 이 과정을 2번 한다.
    7. 또 다시 물고기를 조절한다.(물고기의 수를 큰 곳에서 작은 곳으로 보냄)
    8. 다시 일렬로 바닥에 놓으면 된다.
    9. 위 과정이 1번 이다

    출력 : 가장 물고기가 많은 칸과 가장 적은 칸의 차이가 k이하가 되려면 어항 정리를 몇번 해야하는지 출력해라
    엄청나구만;; 허허...
"""

N, K = map(int, input().split())
fish_tank = list(map(int, input().split()))
fish_idx = [[0, i, 0] for i in range(N)]

for x in range(len(fish_tank)):
    fish_idx[x][2] = fish_tank[x]


def add_fish():
    """ 물고기가 가장 작은 어항에 물고기를 추가해주는 함수 """
    idx_fish = tank_min(min(fish_tank))

    for x in idx_fish:
        fish_tank[x] += 1


def tank_min(min_value):
    """ 물고기가 가장 작은 어항의 인덱스를 찾아주는 함수 """
    temp = []
    for x in range(len(fish_tank)):
        if fish_tank[x] == min_value:
            temp.append(x)
    return temp


def tank_up():
    """ 왼쪽에 있는 어항을 옆에 있는 어항에 쌓아주는 함수 """
    fish_idx[0] = [1, 1, fish_idx[0][2]]

    # 왼쪽에 있다는 소리는 인덱스 번호가 가장 작다는 소리이다


def rotation_90():
    """ 90도 회전시켜서 위에 올려놓는 함수 """
    # 통째로 돌리는게 맞는듯, 돌려야 하는 부분을 찾아야함
    # k는 돌려야 하는 총개수, i는 증가량, cnt는 증가량 조건
    # 이거 다시 구현해야함
    k = 2
    cnt = 0
    i = 2

    while True:

        temp = find_rotation()
        height = find_height()

        if k / height > len(temp) - k:
            return temp

        for x in range(k):
            for y in range(1, k // height + 1):
                temp[x][1] += y
            for h in range(k // height, 0, -1):
                temp[x][0] = h

        if cnt == 2:
            i += 1
            cnt = 0
        k += i
        cnt += 1


def find_rotation():
    """
    회전시켜야 하는 부분을 찾아주는 함수
    두개 이상 쌓여있는 부분을 찾아주면 됨
    """
    temp = sorted(fish_idx, key=lambda x: (x[1], x[0]))

    return temp


def find_height():
    """ 회전시킬때 높이를 찾아주는 함수 -> 2개 이상 쌓여있는게 몇개 인지 찾아주는 함수 """
    height = 0
    cnt = 0
    for x in range(1, len(fish_idx)):
        if fish_idx[x - 1][1] == fish_idx[x][1]:
            cnt += 1

        if fish_idx[x - 1][1] != fish_idx[x][1] and cnt >= 1:
            height += 1
            cnt = 0

    return height


# print(fish_tank)
# add_fish()
# print(fish_tank)
# print(fish_idx)
tank_up()
# print(fish_idx)
print(find_rotation())
print(find_height())
# print(rotation_90())

# 나는 인덱스로 접근할 것
# 현황


# 고려안한것 -> 회전시킬 때 2개 이상 쌓여있는지 확인 안함 => 무조건 2개 이상 쌓여있다고 가정 하고 하는 것임, 그리고 그것은 가장 왼쪽것이라고 가정한거임
# 모든 가정은 무조건 왼쪽에서 하기때문에 정렬 등 다 안하고 왼쪽이 제일 작다는 기준으로 하는 것임
# 회전이 되는 어항의 개수는 2번씩 할때마다 증가하는 수가 1개씩 늘어남
# 회전시킬때 무조건 0을 기준으로 하면 될듯 -> 재귀를 들어가는게 제일 좋은 방법일거 같음 -> 0,0 의 값만 바꾸고 나머지는 그거에 맞게 알아서 바뀌어짐
# 이거 계산할때 인덱스 헷갈리지 말것 -> 지금 엄청 헷갈림 하하
# 회전시키는 것을 찾을때 정렬을 해서 계산하면 됨
# 90도 돌려야함;; 허허
# 싹다 지우고 다시 하기