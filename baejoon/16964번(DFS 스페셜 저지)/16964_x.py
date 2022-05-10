# DFS 스페셜 저지
# 입력 받는 것이 dfs의 출력 순서와 같으면 1 아니면 0을 출력하면 됨

N = int(input())
graph = [[] for _ in range(N+1)]
while True:
    node = list(map(int,input().split()))
    if len(node) == 2:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])
    else:
        break

visited = [False for _ in range(N+1)]
result = []
def dfs(start):
    if visited[start] == True:
        return
    result.append(start)
    visited[start] = True
    for x in graph[start]:
        if not visited[x]:
            dfs(x)

            
            
dfs(1)

# 문제점 - dfs로 가는 방법이 여러가지가 있는데, 이를 전부다 봐야함 -> 깊이가 같을때 순서가 바뀌는 경우도 고려해야함

    