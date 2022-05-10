# 게리맨더링
# 구역은 1부터 N번까지 번호로 매겨져 있음
# 구역을 두 개의 선거구로 나눠야 하고 각 구역은 두 선거구 중 하나에 포함되어야 함
# 선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다
# 두 선거구에 포함된 인구 차이의 최소값을 출력해라
# 만약에 두 선거구로 나눌 수 없을때 -1을 출력해라
from collections import deque

N = int(input())
temp = list(map(int,input().split()))
population = [0]
for x in temp:
    population.append(x)
graph = [[0]]
for _ in range(N): # 만약에 틀렸는데 도저히 모르겠으면 이거 수정하기 -> 동떨어진 선거구가 있을 수도 있다
    a = list(map(int,input().split()))
    if len(a) == 1:
        pass
    else:
        graph.append(a[1:])

visited = [False] * (N+1)

def bfs(start):
    '''구역을 나눠주는 함수'''
    pass
    

def main():
    if len(graph) == 1:
        return -1
    
 
    
# 우선 그냥 풀고 그냥 푼 코드에서 비트 연산자가 필요한 부분은 비트연산자로 바꾸기 -> 그냥도 못풀겠다....;
# 조합으로 풀면 되는데 아무리 생각해도 비트마스킹으로 푸는 방법은 떠오르질않네 -> 비트마스킹을 활용한 조합으로 풀면됨
# bfs,dfs로 나눌 수 있는 모든 부분으로 나누고, 그 중 최소값을 구하기
# 만약에 나눌 수 있는 부분이 없으면 -1 출력

# 나중에 하기