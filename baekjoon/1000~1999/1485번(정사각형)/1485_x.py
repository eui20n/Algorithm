# 정사각형
# 좌표 4개가 주어질때 정사각형을 만들 수 있으면 1, 아니면 0을 출력해라
T = int(input())
for _ in range(T):
    square = []
    for _ in range(4):
        a,b = map(int,input().split())
        square.append([a,b])
    
    square.sort(key = lambda x:x[0])
    
    if abs(square[0][0] - square[1][0]) + abs(square[0][1] - square[1][1]) == abs(square[1][0] - square[2][0]) + abs(square[1][1] - square[2][1]) == abs(square[2][0] - square[3][0]) + abs(square[2][1] - square[3][1]) == abs(square[3][0] - square[4][0]) + abs(square[3][1] - square[4][1]):
        print(1)
    else:
        print(0)
    
# 허허;;
    