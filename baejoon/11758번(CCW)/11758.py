# CCW
# 3개의 좌표가 주어지는데, 이 좌표들이 시계방향인지 아닌지를 출력하면 됨
# 반시계 방향 1, 일직선 0, 시계방향 -1

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

ccw = (b[0] - a[0])*(c[1] - a[1]) - (c[0] - a[0])*(b[1] - a[1])
if ccw < 0:
    print(-1)
elif ccw == 0:
    print(0)
else:
    print(1)
    
    
# ccw 알고리즘이 있음, 벡터의 외적을 이용한 것인데 그것을 활용하면 풀 수 있음