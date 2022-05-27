a = list(map(int,input().split()))
sum_num = 0
for x in a:
    sum_num += x**2
print(sum_num % 10)