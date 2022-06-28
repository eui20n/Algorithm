# 패션왕 신해빈
# 설명 생략

T = int(input())
for i in range(T):
    N = int(input())
    kind = []
    for _ in range(N):
        a,b = map(str,input().split())
        kind.append(b)
    
    new_kind = []
    for x in kind:
        if x not in new_kind:
            new_kind.append(x)
            
    count_kind = [1] * len(new_kind)
    for x in range(len(new_kind)):
        count_kind[x] += kind.count(new_kind[x])
        
    result = 1
    for x in count_kind:
        result *= x
        
    print(result -1 )
    
    