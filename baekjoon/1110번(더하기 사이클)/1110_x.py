# 더하기 사이클
# 만약에 한자리 수면 0을 붙여 2자리 수로 만들고 그 수의 각 자리를 더한 수와 그 수의 가장 오른쪽 수로 새로운 수를 만듬
# 위의 과정을 통해서 몇번 만에 원래의 수가 나오는지 출력해라

N = list(map(int,input()))
new_num = N[0]
count = 0
while True:
    num = list(new_num)
    new_num = 0
    if len(num) == 1:
        num.append('0')
    for x in num:
        new_num +=int(x)
    new_num = int(num[len(num)-1] + str(new_num))
    if new_num == N[0]:
        print(count)
        break
    count +=1
        
    
# 다음에 풀기ㅠㅠ    