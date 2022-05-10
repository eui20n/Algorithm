# 4연산
# 아래의 연산을 이용하여 정수 s를 t로 바꾸는데 필요한 연산 횟수의 최소 값을 구하시오
# 1. s = s + s;(이 연산을 수행하면 + 출력)
# 2. s = s - s;(이 연산을 수행하면 - 출력)
# 3. s = s * s;(이 연산을 수행하면 * 출력)
# 4. s = s / s;(이 연산을 수행하면 / 출력, 이 연산은 s가 0이 아닐때만 사용 가능)
# 만약 위의 연산으로 만들지 못하면 -1을 출력

from collections import deque

S,T = map(int,input().split())

def bfs(S,T):
    visited = [S]
    if S == T:
        return 0
    if T == 0:
        return '-'
    if T < 0:
        return -1
    q = deque()
    q.append([S,''])
    while q:
        p = q.popleft()
        for z in range(4):
            if p[0] >= 10**10:
                break
            if z == 0 and (p[0]*p[0]) not in visited:
                q.append([p[0] * p[0], p[1] + '*'])
                visited.append(p[0]*p[0])
            if z == 1 and (p[0]+p[0]) not in visited:
                q.append([p[0] + p[0], p[1] + '+'])
                visited.append(p[0]+p[0])
            if z == 2: pass
                #q.append([p[0] - p[0], p[1] + '-'])
            if z == 3 and p[0] != 0 and (p[0]/p[0]) not in visited:
                q.append([int(p[0] / p[0]), p[1] + '/'])
                visited.append(p[0]/p[0])
        if p[0] == T:
            return p[1]
    return -1
        
print(bfs(S,T))

