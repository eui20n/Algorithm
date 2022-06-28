# 최단경로
# 방향 그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성해라
# 단, 모든 간선의 가중치는 10이하의 자연수 이다

# 다익스트라 구현을 위해서 heapq 라이브러리에서 필요한 함수 호출
from heapq import heappush,heappop

V,E = map(int,input().split())
start_v = int(input())
# 가중치와 가는 노드의 방향을 받아줄 graph를 생성해줌
graph = [[] for _ in range(V+1)]

# 그래프에 a노드에서 b노드로 가는 가중치 c를 입력 받아서 넣어줌
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])

# 거리는 초기값을 무한대로 해줌
distance = [float('inf')] * (V+1)


def dijkstra(start_v):
    # q 자료구조를 만들기 위해서 빈 리스트 생성
    q = []
    # q에 거리(가중치) 0과 시작점 start_v를 넣어줌
    heappush(q,[0,start_v])
    # 시작점의 거리(가중치)를 0으로 해줌 -> 다른 점은 다 무한대 이기 때문에 시작점이 가장 작은 점이 됨
    distance[start_v] = 0
    # q가 비어있지 않으면 계속 반복하고 비어있으면 끝냄
    while q:
        # 그 노드의 거리와 현재 위치를 dist와 now에 넣어줌
        dist,now = heappop(q)
        # 만약에 현재 거리가 dist보다 작으면 안함
        if distance[now] < dist:
            continue
        # 노드들 간의 거리를 비교
        for i in graph[now]:
            # cost에 거리 + i[1]를 넣어줌 -> i[1]번째는 그 노드가 다른 노드로 가는 것의 가중치임
            cost = dist + i[1]
            # 비교하고 작으면 바꿔줌
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 다시 q에 값을 갱신해줌
                heappush(q,[cost,i[0]])
                
# 함수 실행
dijkstra(start_v)
# 출력
for x in range(1,len(distance)):
    if distance[x] == float('inf'):
        print('INF')
    else:
        print(distance[x])
