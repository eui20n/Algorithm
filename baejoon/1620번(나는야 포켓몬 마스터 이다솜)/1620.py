# 나는야 포켓몬 마스터 이다솜
# 첫째줄에는 포켓몬 도감에 수록되어 있는 포켓몬 수 N이랑 맞춰야 하는 문제의 수 M
# 두번째줄에는 N개의 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬이 한줄씩 있음
# 그 다음 줄에는 초 M개의 줄에 맞춰야하는 문제가 입력으로 들어옴
# 문제가 숫자면 그 숫자에 맞는 포켓몬을 출력하고, 이름이면 그 이름이 해당하는 포켓몬을 출력

N,M = map(int,input().split())
poket = []
for _ in range(N):
    a = input()
    poket.append(a)

solved = []
for _ in range(M):
    problem = input()
    if problem[0] == '1' or problem[0] == '2' or problem[0] == '3' or problem[0] == '4' or problem[0] == '5' or problem[0] == '6' or problem[0] == '7' or problem[0] == '8' or problem[0] == '9':
        solved.append(poket[int(problem)-1])
    else:
        solved.append(poket.index(problem) + 1)
for x in solved:
    print(x)