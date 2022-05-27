# 통계학
# 수가 주어졌을때 산술평균, 중앙값, 최빈값, 범위를 구하여라
import sys
N = int(sys.stdin.readline())
num = []

for _ in range(N):
    a = int(sys.stdin.readline())
    num.append(a)
    
num.sort()

# 산술평균
num_mean = round(sum(num)/len(num))

# 중앙값
num_mid = num[len(num)//2]

# 최빈값
        

        

