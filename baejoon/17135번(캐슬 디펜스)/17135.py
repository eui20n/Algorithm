# 캐슬 디펜스
# 격자판의 R번행 바로 아래의 모든 칸에는 성이 있다
# 성을 지키는 궁수는 3명 있는데, 거리제한이 있다, 이 값은 입력으로 들어온다
# 궁수들 각각은 하나의 적만 공격할 수 있고, 그 적이 공통된 적이 될 수 있다
# 만약 궁수 기준으로 가장 가까운 적이 여러명이면 가장 왼쪽의 적을 공격한다
# 공격당한 적은 필드위에서 제거가 된다
# 모든 적이 격자판 아래로 내려가면 끝이 난다
# 이때 궁수가 잡을 수 있는 적의 최대값을 구해라

from collections import deque
from itertools import combinations
from copy import deepcopy

R,C,D = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(R)]
archer = list(combinations(range(C),3)) # 궁수의 위치


def attack(x_1,x_2,x_3):
    ''' 궁수가 적을 공격하고, 적이 없어지는 함수 '''
    new_graph = deepcopy(graph)
    
    count_enemy = 0
    new_graph = deque(new_graph)
    
    
    archer_loc = [[R,x_1],[R,x_2],[R,x_3]]
    
    while True:
        game_turn = 0
        count = 0
        for x in range(R):
            for y in range(C):
                if new_graph[x][y] == 1:
                    count +=1
                    
        if count == 0:
            return count_enemy
        
        # 범위 안에 적이 어디에 있는지 알아야함
        enemy_loc = []                    
        for x in range(R-1,game_turn-1,-1):
            for y in range(C):
                if new_graph[x][y] == 1:
                    enemy_loc.append([x,y])
    
        # 공격을 동시에 함 -> 미리 공격할 리스트를 만들고 공격한 후 이 리스트의 값을 없애야함
        enemy = [[] for _ in range(3)]
        enemy_dist = [[100] for _ in range(3)]
        for z in enemy_loc:
            for y in range(len(archer_loc)):
                if D < R:
                    if abs(z[0]-archer_loc[y][0]) + abs(z[1] - archer_loc[y][1]) <= enemy_dist[y][0] and abs(z[0]-archer_loc[y][0]) + abs(z[1] - archer_loc[y][1]) <= D:
                        if abs(z[0]-archer_loc[y][0]) + abs(z[1] - archer_loc[y][1]) == enemy_dist[y][0]:
                            if enemy[y][1] > z[1]:
                                enemy[y] = [z[0],z[1]]
                            else:
                                pass
                        else:
                            enemy_dist[y][0] = abs(z[0]-archer_loc[y][0]) + abs(z[1] - archer_loc[y][1])
                            enemy[y] = [z[0],z[1]]
                else:
                    if abs(z[0]-archer_loc[y][0]) + abs(z[1] - archer_loc[y][1]) <= enemy_dist[y][0] and abs(z[0]-archer_loc[y][0]) + abs(z[1] - archer_loc[y][1]) <= R:
                        if abs(z[0]-archer_loc[y][0]) + abs(z[1] - archer_loc[y][1]) == enemy_dist[y][0]:
                            if enemy[y][1] > z[1]:
                                enemy[y] = [z[0],z[1]]
                            else:
                                pass
                        else:
                            enemy_dist[y][0] = abs(z[0]-archer_loc[y][0]) + abs(z[1] - archer_loc[y][1])
                            enemy[y] = [z[0],z[1]]              
        
        
        # 적을 공격함
        for x in enemy:
            for z in new_graph:
                if len(x) == 0:
                    break
                if new_graph[x[0]][x[1]] == 1:
                    new_graph[x[0]][x[1]] = 0
                    count_enemy +=1
                
        # 내림
        new_graph.appendleft([0 for _ in range(C)])
        new_graph.pop()
        
                    

result = 0
for z in archer:
    num = attack(z[0],z[1],z[2])
    if num > result:
        result = num
print(result)


# 먼저 사정거리 위의 값은 필요 없는 값이니 무시하고, 내려오는 연산 대신에 pop으로 빼는 연산을 할것, 그리고 추가는 appendleft로 할것
# 궁수의 위치는 반복문을 이용해서 구하기, 아니면 조합을 이용해서 구하기
# 진짜 실력이 상승하면 궁수의 위치 비트마스킹으로 해보기