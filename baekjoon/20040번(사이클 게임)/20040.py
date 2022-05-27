"""
    문제 이름 : 사이클 게임
    URL : https://www.acmicpc.net/problem/20040
    ----------------------------------------------
    <문제 설명>
    사이클을 만들면 되는데 사이클은 아래의 조건을 만족한다
    - C에 속한 임의의 선분의 한 끝점에서 출발하여 모든 선분을 한 번씩만 지나서 출발점으로 되돌아올 수 있다

    출력하고 싶은 것은 몇 번째 차례에서 사이클이 완성되었는지 or 아니면 아직 사이클이 없는지 출력하면 된다
    만약에 사이클이 없다면 0을 출력하면 되고, 사이클이 있다면 언제 사이클이 만들어 졌는지 출력하면 된다

"""

n, m = map(int, input().split())
graph = []
for x in range(m):
    a = list(map(int, input().split()))
    graph.append(a)

parents = list(range(n))
cnt_game = 0


def find(x):
    if x == parents[x]:
        return x
    else:
        y = find(parents[x])
        parents[x] = y
        return y


def union(x, y, idx):
    global cnt_game
    x = find(x)
    y = find(y)
    if x != y:
        parents[max(x, y)] = min(x, y)
    elif cnt_game == 0:
        cnt_game = idx


for i in range(m):
    union(graph[i][0], graph[i][1], i + 1)

print(cnt_game)


