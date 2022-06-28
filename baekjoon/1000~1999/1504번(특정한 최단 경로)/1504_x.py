# 특정한 최단 경로
# 방향성이 없는 그래프가 주어진다
# 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다
# 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 하는 것이다
# 한번 이동했던 간선도 다시 이동할 수 있지만 반드시 최단 경로로 이동해야 한다
# 그러한 경로가 없을때는 -1을 출력해라 -> 서로 이러져 있지 않다는 의미
from heapq import heappush,heappop

N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

go_node = list(map(int,input().split()))
go_node.append(1)
go_node.sort()

#distance = [float('inf')] * (N+1)

def dijkstra(start): # start  = 1 임
    q = []
    heappush(q,[0,start])
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist: # 방문처리
            continue
        for z in graph[now]:
            cost = dist + z[1]
            if cost < distance[z[0]]:
                distance[z[0]] = cost
                heappush(q,[cost,z[0]])
                
    
cost = 0
for x in range(len(go_node)):
    result = float('inf')
    distance = [float('inf')] * (N+1)
    dijkstra(go_node[x])
    if x == len(go_node)-1: break
    for y in range(x,len(go_node)):
        if distance[y] == 0:
            pass
        elif result > distance[y]:
                result = distance[y]
    cost += result

print(cost + distance[N])

    
# 만약 다익스트라로 할 경우 최악의 경우 시간 복잡도(O(ElogV)) - 130만, 방향이 없으니 x2 = 260만 => 넉넉함, 다른 연산을 걱정없이 해도 될 정도임

# 첫번째 생각 -> 특정 노드로 가는 곳의 최단 경로를 구하고 합친다
# 다음에 다시 풀기
    
    
    
