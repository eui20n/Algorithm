# 두 수의 합
# 두 수의 합이 원하는 수가 되게 하는 쌍이 몇개 있는지 출력하면 됨

N = int(input())
num = list(map(int,input().split()))
want_num = int(input())

count = 0

result = [False for _ in range(2000001)]

for x in num:
    result[x] = True
    
for x in range(1,len(result)):
    if result[x] and result[want_num-x]:
        count +=1
        result[want_num-x] = False
        
print(count)