# N과M_11
# 같은 수를 여러 번 골라도 됨

N,M = map(int,input().split())
num = list(map(int,input().split()))

num = list(set(num))
num.sort()

result = []
num_list = []
#visited = [False] * N

def NM():
    if len(result) == M:
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
    

# 이 문제는 정렬을 잘 사용해야함, 그리고 중복을 제거하기 위해서 집합을 사용했음