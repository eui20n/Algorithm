# 잃어버린 괄호
# 괄호를 적절한 곳에 배치해서 연산식의 값이 최소가 되게 하는 문제
# 최소가 되는 방법 -> +가 -가 되면 됨, 즉 - 앞에서 다음 - 전까지 괄호를 치면 됨

N = list(input())
n = []
number = []
for x in N:
    if x == '-' or x == '+':
        number.append(''.join(n))
        number.append(x)
        n = []
    else:
        n.append(x)

number.append(''.join(n))

def change(): # 조금 고치기
    count = 0
    for x in range(len(number)):
        if number[x] == '-' and count == 0:
            count = 1
        if number[x] == '+' and count == 1:
            number[x] = '-'
            
def com():
    # 연산만 해주면 됨
    num = 0
    plus = 1
    for x in number:
        if x == '+':
            plus = 1
        elif x == '-':
            plus = -1
        else:
            num += int(x)*plus
    return num

def main():
    change()
    print(com())
    
main()
    
            


