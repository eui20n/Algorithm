# 괄호를 찾는 문제
# 괄호가 제대로 안닫힌 문자열에는 NO, 제대로 닫힌 문자열은 YES를 출력하면 됨

T = int(input())
for i in range(T):
    a = list(input())
    b = []
    c = 1
    d = 1
    for x in a:
        if x == '(':
            b.append(c)
            c+=1
        elif x == ')':
            b.append(d)
            d+=1
        if d > c:
            break
    if b.count(max(b)) == 2:
        print('YES')
    else:
        print('NO')
        
# 내가 하는 나름대로의 해석
# C 와 D는 (와 )의 역활을 하는 것으로 )가 먼저 오면 끝이 나게 만듬
# 또한 (와 )의 수가 맞지 않으면 NO가 출력이 되도록 함
# 위의 두 조건이면 모든 조건이 걸러짐
    