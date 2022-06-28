# 나이순 정렬
# 나이가 어린 순으로 정렬하면 됨
# 만약에 나이가 같으면 위에 있는거 먼저 나오면 됨

N = int(input())
a = [list(input().split()) for _ in range(N)]

for x in range(len(a)):
    a[x][0] = int(a[x][0])
    
a.sort(key = lambda x:(x[0]))

for x in range(len(a)):
    print(a[x][0],a[x][1])