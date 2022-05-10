# N과M_12
# N과M_11에서 나온 수열을 내림차순으로 출력하면 됨

N,M = map(int,input().split())
num = list(map(int,input().split()))

num = list(set(num))
num.sort()

result = []
num_list = []
#visited = [False] * N

def NM():
    if len(result) == M:
        if result == sorted(result):
            a = ' '.join(map(str,result))
            num_list.append(a)
        return
    for x in num:
        result.append(x)
        NM()
        result.pop()
        
NM()
for x in num_list:
    print(x)