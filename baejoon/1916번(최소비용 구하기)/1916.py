# 최소비용 구하기
# N개의 도시가 있다
# 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있고 , 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 비용을 최소화 시키려고 한다
# A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라
from heapq import heappush,heappop

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
start,end = map(int,input().split())
    
distance = [float('inf')] * (N+1)

def dijkstra(start):
    q = []
    heappush(q,[0,start])
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q,[cost,i[0]])
                
dijkstra(start)
print(distance[end])
    
    
    
    
    
    