# 알파벳
# 세로 R 가로 C 칸으로 된 모양의 보드의 각 칸에 대문자 알파벳이 하니씩 적혀 있고, 좌측 상단(0,0)에는 말이 놓여 있다
# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다
# 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다
# (0,0)에서 시작해서 말이 최대한 몇 칸을 지날 수 있는지 출력해라
# 이때 (0,0)도 지나간 칸에 포함이 된다

R,C = map(int,input().split())
graph = [list(map(str,input())) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count_list = [0]
group = {graph[0][0]}


def dfs(x,y,count):
    #print(group)
    for z in range(4): 
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] not in group:
            #group.append(graph[nx][ny])
            group.add(graph[nx][ny])
            count +=1
            dfs(nx,ny,count)
            count -=1
            #group.pop()
            group.remove(graph[nx][ny])
        else:
            if count_list[0] < count:
                count_list[0] = count
    return
            
            

dfs(0,0,1)
for x in count_list:
    print(x)

# 이 문제를 풀면서 깨달은 점
# 집합(set)도 in 연산이 가능 -> list로 할땐 시간 복잡도가 N이였지만 집합은 1임
# 함수의 매개변수도 은근히 시간을 잡아먹음 -> 매개변수를 빼니까 아슬아슬하게 통과함
# 이 문제에서는 방문처리가 당연히 필요 없었음;; 허허
