# 어른 상어
# N x N 격자판 위에서 상어가 움직인다
# 상어는 아래의 규칙에 따라서 움직인다
# 1. 먼저 현재 위치에 본인의 냄새를 뿌린다
# 2. 방향에 따라서 움직인다
# 2-1. 냄새가 없는 칸이 우선순위
# 2-2. 위와 같은 칸이 없으면 자신의 냄새가 있는 칸으로 간다
# 2-3. 만약에 위와 같은 경우가 여러경우일 경우 상어마다 가지고 있는 특정한 우선순위를 따른다
# 2-4. 만약에 상어가 겹치는 번호가 작은 상어가 남고 다른 상어는 사라진다
# 1번 상어만 남을때까지 걸리는 시간을 출력해라, 만약에 1000초 동안 이러한 경우가 없으면 -1을 출력해라
# 만약에 상어가 다른 냄새에 있는 칸으로 가면 그 칸의 냄새는 현재 온 상어의 냄새를 따른다
# 이동 순서
# 현재 칸에 냄새 뿌림 -> 규칙에 따라서 움직임 -> 만약에 겹치는 상어가 있으면 번호가 낮은 상어가 남음
# 냄새는 k시간 후에 사라진다
# 방향은 1(위) 2(아래) 3(왼쪽) 4(오른쪽)
# 우선순위를 입력할때의 순서 - 위, 아래, 왼쪽, 오른쪽

N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
shark_dir = list(map(int, input().split()))
dir_priority = [[] for _ in range(M)]
for x in range(M):
    for _ in range(4):
        a = list(map(int, input().split()))
        dir_priority[x].append(a)

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]


# 현재위치에 냄새를 뿌림
def shark_smell(graph, shark_smell_graph, shark_smell_check_graph):
    '''현재 위치에 냄새를 뿌리는 연산'''
    for x in range(N):
        for y in range(N):
            if graph[x][y] != 0:
                shark_smell_graph[x][y] = K
                shark_smell_check_graph[x][y] = graph[x][y]


# 상어가 이동하는 함수, 만약에 시간이 많이 걸리면 상어의 위치를 미리 저장하고 위치만 꺼내는 식으로 할것, 우선순위인 방향으로 감
# 헷갈리게 안하기 위해서 graph에서만 상어를 지우고, 그 외 정보는 안지움
def shark_move(graph, dir_priority, shark_dir, shark_smell_check_graph):
    '''상어 이동하고 만약 겹치면 크기가 작은 상어는 사라지는 함수'''
    new_graph = [[0 for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if graph[x][y] != 0:  # 현재위치에 상어가 있다면
                count = 0
                for z in dir_priority[graph[x][y] - 1][shark_dir[graph[x][y] - 1] - 1]:  # 우선 순위대로 방향을 정해준 것
                    nx = x + dx[z]
                    ny = y + dy[z]
                    if 0 <= nx < N and 0 <= ny < N and shark_smell_check_graph[nx][ny] == 0:  # 냄새가 없는 칸을 우선순위로 봄
                        if new_graph[nx][ny] != 0 and new_graph[nx][ny] < graph[x][y]:  # 상어가 있고 그 상어의 번호가 더 작을때 -> 더 큰 번호의 상어는 사라짐
                            count += 1
                            break
                        elif new_graph[nx][ny] != 0 and new_graph[nx][ny] > graph[x][y]:  # 상어가 있고 그 상어의 번호가 더 클때 -> 더 큰 번호의 상어는 사라짐
                            count += 1
                            shark_dir[graph[x][y] - 1] = z
                            new_graph[nx][ny] = graph[x][y]
                            break
                        elif new_graph[nx][ny] == 0:  # 그 칸이 빈칸일때 그냥 가면 됨, 위의 조건으로 냄새도 없는 칸임
                            count += 1
                            shark_dir[graph[x][y] - 1] = z
                            new_graph[nx][ny] = graph[x][y]
                            break

                if count == 0:  # 갈곳이 없다는 소리
                    for z in dir_priority[graph[x][y] - 1][shark_dir[graph[x][y] - 1] - 1]:
                        nx = x + dx[z]
                        ny = y + dy[z]
                        if 0 <= nx < N and 0 <= ny < N and shark_smell_check_graph[nx][ny] == graph[x][y]:
                            shark_dir[graph[x][y] - 1] = z
                            new_graph[nx][ny] = graph[x][y]
                            break
    new_graph
    return new_graph


def after_sec(shark_smell_graph, shark_smell_check_graph):
    '''1초가 지나서 상어가 뿌린 냄새를 1씩 줄이는 연산'''
    for x in range(N):
        for y in range(N):
            if shark_smell_graph[x][y] != 0:
                shark_smell_graph[x][y] -= 1
                if shark_smell_graph[x][y] == 0:
                    shark_smell_check_graph[x][y] = 0


def main(graph):
    '''위의 함수들을 합할 함수로 실직적인 실행을 담당하는 함수'''
    time = 0

    graph = graph

    # 냄새를 몇번 남았는지 담아둘 리스트 생성
    shark_smell_graph = [[0 for _ in range(N)] for _ in range(N)]

    # 뿌려진 냄새가 어느 상어의 냄새인지 확인해주는 리스트 생성
    shark_smell_check_graph = [[0 for _ in range(N)] for _ in range(N)]

    # 인덱스를 번호를 맞추려고 0은 비우고 방향 벡터를 설정한 것
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    # 1000초 이니까 최대 1000번 반복할것
    while time != 1000:

        count_one = 0
        time += 1
        shark_smell(graph, shark_smell_graph, shark_smell_check_graph)
        graph = shark_move(graph, dir_priority, shark_dir, shark_smell_check_graph)
        after_sec(shark_smell_graph, shark_smell_check_graph)
        for x in range(N):
            for y in range(N):
                if graph[x][y] != 0:
                    count_one += 1

        if count_one == 1:
            return time

    return -1


print(main(graph))

# 만약에 우선순위를 정했는데도 못가는 곳이 있으면 어떻게 하는가? -> 절대 그럴 경우 없음, 자기가 온 곳엔 자기의 냄새가 있음
# 구현해야하는 함수
# 1. 냄새를 뿌리는 함수
# 2. 상어가 이동하는 함
# 상어는 사라져도 남새는 남음
# 냄새가 먼저 사라지나? 상어가 먼저 움직이나? -> 상어가 먼저임
