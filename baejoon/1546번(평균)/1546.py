T = int(input())
a = list(map(int,input().split()))
sum_num = 0
max_num = max(a)
for x in a:
    sum_num += (x/max_num)*100

print(sum_num/T)
