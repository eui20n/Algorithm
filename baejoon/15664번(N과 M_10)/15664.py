# N과M_10
# N과M_9와 동일하나 수열은 내림차순이여야 한다

N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
result = []
num_list = []
visited = [False] * N

def NM(start):
    if len(result) == M:
        if result == sorted(result):
            a = ' '.join(map(str,result))
            if a not in num_list:
                num_list.append(a)
        return
    for x in range(start,N):
        if not visited[x]:
            visited[x] = True
            result.append(num[x])
            NM(start+1)
            result.pop()
            visited[x] = False
           
NM(0)
for x in num_list:
    print(x)
        