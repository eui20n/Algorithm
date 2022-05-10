# 치킨 배달
# 크기가 N x N인 도시가 있고 도시의 각 칸은 빈칸, 치킨집, 집 중 하나이다
# 도시의 칸은 (r,c)와 같은 형태로 나타내고, r과 c는 1부터 시작이다
# 이 도시 사람들은 치킨을 매우 좋아한다, 따라서 치킨거리 라는 말을 주로 사용한다
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리다, 즉 치킨 거리는 집을 기준으로 정해지며 각각의 집은 치킨 거리를 가지고 있다
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합니다(거리는 |r1-r2| + |c1-c2|)
# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업 시켜야 한다고 할때
# 어떻게 고르면 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성해라
# 0은 빈칸, 1은 집, 2는 치킨 집이다

from collections import deque
from itertools import combinations

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

chicken_loc = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 2:
            chicken_loc.append([x,y])
            
def chicken_home(chicken_list):
    pass

    
# bfs쓰지말기
# 비트 마스크 공부해서 비트 마스크로 나중에 해보기
# 조합 사용하지 말고 하기