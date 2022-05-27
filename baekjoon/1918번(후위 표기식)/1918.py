# 후위 표기식
# 중위 표기식 -> 우리가 쓰는 수식을 쓰는 방법(a+b)
# 중위 표기식이 주어지면 그 식을 후위 표기식으로 바꿔라(a+b -> ab+)

word = input()

stack = []
result = ''

for x in word:
    if x.isalpha():
        result += x
    elif x == '(':
        stack.append(x)
    elif x == '*' or x == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result += stack.pop()
        stack.append(x)
    elif x == '+' or x == '-':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(x)
    elif x == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()

for x in range(len(stack)-1,-1,-1):
    if stack[x] != '(' and stack[x] != ')':
        result += stack[x]


print(result)
    
    
# 연산의 우선 순위
# 1. 괄호
# 2. * /
# 3. + -
# 이 문제에서 꼭 알아야 하는 함수 isalpha() -> 영어 인지 아닌지 검사해주는 함수

