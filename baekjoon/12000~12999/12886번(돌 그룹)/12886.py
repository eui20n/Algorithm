# 돌 그룹
# 크기가 다른 돌 3개가 있다
# 이 돌을 크기가 같게 하면 된다
# 연산은 아래와 같다
# 크기가 다른 두 돌을 고른다. 작은 돌을 X, 큰 돌을 Y라고 할때
# 작은 돌은 X + X 개로 늘어나고, Y는 Y - X로 줄어든다
# 위의 과정을 통해서 돌의 크기를 모두 같게 할 수 있으면 1 아니면 0을 출력해라
from collections import deque

a,b,c = map(int,input().split())

def bfs(a,b,c):
    if (a+b+c)%3 != 0:
        return 0
    
    
    q = deque()
    q.append([a,b,c])
    count = 0
    while q:
        p = q.popleft()
        # p를 계속 크기 순으로 정렬해줌
        p.sort()
        for z in range(3):
            if z == 0 and p[0] != p[1]:
                q.append([p[0]+p[0],p[1]-p[0],p[2]])
            if z == 1 and p[0] != p[2]:
                q.append([p[0]+p[0],p[1],p[2]-p[0]])
            if z == 2 and p[1] != p[2]:
                q.append([p[0],p[1]+p[1],p[2]-p[1]])
        count +=1
        if count == 1000000:
            return 0
        if p[0] == p[1] == p[2]:
            return 1
    return 0

print(bfs(a,b,c))
    
    
# count 빼야함 -> 그냥 코드가 맞는지 보려고 한건데 허허;;;;
    