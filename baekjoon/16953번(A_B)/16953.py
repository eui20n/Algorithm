# A -> B
# 가능한 연산은 2가지 이다
# 1. 2를 곱한다
# 2. 수의 오른쪽에 1을 추가한다(더하는거 아님, 5 -> 51 이런식으로)
# 위의 연산을 수행해서 A -> B로 갈 수 있는 방법의 최솟값을 구하여라
# 만약에 A -> B로 가지 못할 경우에는 -1을 출력해라

from collections import deque

A,B = map(int,input().split())

def change_num(A,B):
    q = deque()
    depth = 1
    q.append([A,depth])
    while q:
        p = q.popleft()
        #print(p)
        if p[0] == B:
            return p[1]
        for x in range(2):
            if len(str(p[0])) >= 10: # B의 최대값이 10^9이기 때문에 계속해서 추가되는 p[0]의 길이가 9가 넘어가면 for문을 멈춤 -> 이 과정을 반복하면 q가 빈 리스트가 되기때문에 while문 종료됨
                break
            if x == 0:
                q.append([int(str(p[0]) + '1'),p[1] + 1])
            if x == 1:
                q.append([p[0]*2,p[1] + 1])
    return -1
                
print(change_num(A,B))







