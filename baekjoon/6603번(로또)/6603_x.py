# 로또
# K개의 수의 집합에서 나올 수 있는 모든 부분집합을 구하면 됨
    
def lotto(set_num):
    if len(set_num) == 6:
        set_num.sort()
        for x in result:
            if set_num == x:
                return 1
        result.append(set_num)
        return 1
    
    for x in set_num:
        new_list = set(set_num) - set([x])
        lotto(list(new_list))
        
while True:
    num = list(map(int,input().split()))
    T = num[0]
    set_num = num[1:len(num)]
    if T == 0:
        break
    result = []
    lotto(set_num)
    result.sort()
    for x in result:
        print(' '.join(map(str,x)))
    print('')
    
        
# 사전 순으로 출력하기
    
    
    
