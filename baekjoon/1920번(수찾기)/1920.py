# 수 찾기
# 수가 존재하면 1 아니면 0 출력
n = int(input())
num_1 = set(map(int,input().split()))
m = int(input())
num_2 = list(map(int,input().split()))
result = []

for x in range(len(num_2)):
    if num_2[x] in num_1:
        result.append(1)
    else:
        result.append(0)
        
for x in result:
    print(x)