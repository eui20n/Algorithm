import sys
T = int(sys.stdin.readline())
N = [0] * 10001
for _ in range(T):
    a = int(sys.stdin.readline())
    N[a] +=1

count = 0
while count != len(N):
    if N[count] == 0:
        pass
    else:
        for _ in range(N[count]):
            print(count)
    count +=1
    
# 공간복잡도와 시간복잡도 모두 생각하는 문제