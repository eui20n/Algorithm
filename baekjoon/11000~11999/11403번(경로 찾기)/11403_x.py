# 경로 찾기
# 가중치가 없는 방향 그래프 G가 주어졌을 때, 모든 정점(i,j) 에 대해서, i에서 j로 가는 경로가 있는지 없는지 구해라

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

# 다음에