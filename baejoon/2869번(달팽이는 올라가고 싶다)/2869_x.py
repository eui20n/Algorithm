import sys
A,B,V = map(int,sys.stdin.readline().split())
day = 0
while V > 0:
    V = V - A
    if V <= 0:
        day +=1
        break
    V = V + B
    day +=1
print(day)

# 시간 줄이기