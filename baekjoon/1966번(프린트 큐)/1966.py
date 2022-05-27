from collections import deque

T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    #num = a[M]
    num = M
    count = 0
    q = deque(a)
    
    while q:
        if max(q) != q[0]:
            if num == 0:
                num += len(q)-1
            else:
                num -=1
            q.append(q.popleft())
            
        else:
            count +=1
            if num == 0:
                break
            else:
                q.popleft()
                num -=1
                
    print(count)

    
    
    
    