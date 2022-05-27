# N과M_1
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구해라
# 1부터 N까지 자연수 중에서 중복 없이 M개 고른 수열

N,M = map(int,input().split())

num = []

def NM():
    if len(num) == M:
        for x in num:
            print(x,end = ' ')
        print('')
        return 1
    else:
        for x in range(1,1+N): # 출력해야 하는 리스트를 따로 안만들고 for문 통해서 만듬
            if x not in num:
                num.append(x)
                NM()
                num.pop() # 출력했으면 다시 빼주는 과정
            
NM()

        
        
        
        