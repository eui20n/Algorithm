# 듣보잡
# 듣도 못한 사람의 명단과 보도 못한 사람의 명단이 주어짐
# 이때 듣도 보도 못한 사람의 수와 이름을 사전순으로 출력하면 됨

N,M = map(int,input().split())
dont_listen = set([input() for _ in range(N)])
dont_watch = set([input() for _ in range(M)])

name = []
for x in (dont_listen & dont_watch):
    name.append(x)

name.sort()
print(len(name))
for x in name:
    print(x)
    
# 집합을 이용한 문제로, 만약에 찾고 싶은 연산을 할때 in은 리스트의 요소 수 만큼 반복을 해서 시간이 많이 소요됨
# 하지만, 집합을 이용하면 시간이 적게 걸림
