# 연산자 끼워넣기
# 더하기, 빼기, 곱하기, 나누기를 적절하게 넣어서 수의 배열에 최대값과 최소값을 출력하면 됨
# 다만, 연산에 순서는 앞에 있는 것이 먼저이며 나누기는 몫만 취급함
# 입력의 첫째줄은 수의 개수 둘째 줄은 그 수의 배열 세번째는 더하기, 빼기, 곱하기, 나누기의 수이다
# + - * /

N = int(input())
num = list(map(int,input().split()))
count_num = list(map(int,input().split()))
sdmd = ['+','-','*','/']
sdmd_list = []
num_list = []
visited = [False] * sum(count_num)

for x in range(len(count_num)):
    sdmd_list +=sdmd[x] * count_num[x]
    
def dfs(result):
    if sum(count_num) == 0:
        result_num = num[0]
        #print(result)
        for x in range(len(result)):
            if result[x] == '+':
                result_num = result_num + num[x+1]
            if result[x] == '-':
                result_num = result_num - num[x+1]
            if result[x] == '*':
                result_num = result_num * num[x+1]
            if result[x] == '/':
                if result_num * num[x+1] < 0:
                    result_num = (((result_num) * (-1)) // num[x+1]) * (-1)
                else:
                    result_num = result_num // num[x+1]
        num_list.append(result_num)
        return
    for x in range(0,len(sdmd_list)):
        if not visited[x]:
            if sdmd_list[x] == '+':
                count_num[0] -=1
                visited[x] = True
                result.append(sdmd_list[x])
                dfs(result)
                result.pop()
                count_num[0] +=1
                visited[x] = False
            if sdmd_list[x] == '-':
                count_num[1] -=1
                visited[x] = True
                result.append(sdmd_list[x])
                dfs(result)
                visited[x] = False
                result.pop()
                count_num[1] +=1
            if sdmd_list[x] == '*':
                count_num[2] -=1
                visited[x] = True
                result.append(sdmd_list[x])
                dfs(result)
                visited[x] = False
                result.pop()
                count_num[2] +=1
            if sdmd_list[x] == '/':
                count_num[3] -=1
                result.append(sdmd_list[x])
                visited[x] = True
                dfs(result)
                result.pop()
                visited[x] = False
                count_num[3] +=1
            
            
dfs([])
print(max(num_list))
print(min(num_list))


# 천천히 하기, 어디선가 틀림 => 방문처리 해줄것
# 먼저 할 수 있는 연산자를 모두 다 구함 -> 그 구한 리스트를 가지고 연산을 함 ==> 시간과 메모리의 문제가 나올수도
# ==> 구하는 대로 바로 계산
