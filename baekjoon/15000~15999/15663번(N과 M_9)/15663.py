# N과M_9
# 입력에서 중복되는 수가 생김
N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()

result = []
num_list = []
visited = [False] * len(num)

def NM():
    if len(result) == M:
        a = ' '.join(map(str,result))
        if a not in num_list:
            num_list.append(a)
        return
    for x in range(0,len(num)):
        if not visited[x]:
            result.append(num[x])
            visited[x] = True
            NM()
            result.pop()
            visited[x] = False

def main():
    NM()
    for x in num_list:
        print(x)
        
main()


# 정리 - 방문처리하기 ==> 백트래킹 하는것 처럼 함수에 들어가면 True, 다시 나오면 False해주면 됨
# deepcopy 안쓰는 방법은 result는 계속 바뀌는 값이니까 이 값을 다른 곳에 저장 후 사용하면 됨