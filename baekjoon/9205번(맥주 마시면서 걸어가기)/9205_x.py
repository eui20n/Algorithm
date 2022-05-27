# 맥주 마시면서 걸어가기
# 50M를 가려면 맥주 그 직전에 맥주 한 병을 마셔야 한다(맥주 한 박스에는 20개의 맥주가 있다)
# 도착하는 곳이 매우 멀어 중간에 더 사야한다
# 이때 빈병을 버릴 수 있고, 새로운 맥주를 살 수 있지만 20개가 넘어갈 수 없다
# 입력은 테스트 케이스가 주어지고, 각 테스트 케이스의 첫줄에는 맥주를 파는 편의점의 개수 n이 주어진다
# 그 n + 2개의 줄에는 집, 편의점, 도착점의 좌표가 x,y 로 주어진다
# 두 좌표사이의 거리를 구하는 공식은 맨하튼 거리 공식을 이용한다
# 맥주를 마시면서 도착점에 도착할 수 있으면 'happy', 도착을 못하면 'sad'를 출력해라

# 생각해볼것 - 편의점이 도착하는 곳보다 더 멀리 있는 경우 -> 고려 안해도 될듯

from collections import deque

T = int(input())
for _ in range(T):
    # 입력
    store_num = int(input())
    home = list(map(int,input().split()))
    store = []
    for _ in range(store_num):
        store.append(list(map(int,input().split())))
    festival = list(map(int,input().split()))

            

# 편의점 만나면 어떻게 계산할지 생각 해야함
# 50m를 거면 맥주 1병, 그 중간에 편의점이 있으면 맥주는 20병으로 채워짐
# 시간 초과 해결해야함
