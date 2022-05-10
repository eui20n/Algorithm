# 좌표압축
# 자기 보다 작은 원소가 몇개인가

N = int(input())
num = list(map(int,input().split()))

sorted_num = sorted(list(set(num)))

dic = {sorted_num[x]: x for x in range(len(sorted_num))}

for x in num:
    print(dic[x],end = ' ')
    
# 딕셔너리 활용 문제