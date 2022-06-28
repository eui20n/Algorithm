# 마인크래프트
# 집을 짓어야 하는데, 집을 지으려면 땅이 평평해야한다
# 집터를 N by M 으로 골랐다, 집터 맨왼쪽 좌표는 (0,0)이다
# 1. 좌표 (i,j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다
# 2. 인벤토리에서 블록 하나를 꺼내어 좌표(i,j)의 가장 위에 있는 블록 위에 놓는다
# 1번 작업은 2초가 걸리고, 2번 작업은 1초가 걸린다
# 밤에 좀비가 온다, 최대한 빨리 땅을 다져야 할때 최소 시간과 그 땅의 높이를 출력하기
# 집터 밖에 있는 블록으로는 작업을 할 수 없다
# 입력의 N,M,B는 가로 세로 가지고있는 블록의 수 이다

N,M,B = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

# 블록 얻는 것(1초) get으로, 블록 놓는 것(2초) take로
get = 0
take = 0

block = []
for x in range(N):
    for y in range(M):
        if graph[x][y] not in block:
            block.append(graph[x][y])
            
block_count = [0] * len(block)
for z in range(len(graph)):
    for r in range(len(block_count)):
        block_count[r] += graph[z].count(block[r])
        


