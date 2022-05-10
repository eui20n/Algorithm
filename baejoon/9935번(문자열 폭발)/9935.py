# 문자열 폭발
# 문자열에 폭발 문자열을 심어 놓았다
# 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열을 합쳐지게 된다
# 폭발하는 과정은 아래와 같다
# - 문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 되고, 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다
# - 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다
# - 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다
# 어떤 문자열이 남는지 출력해라
# 만약 남은 문자열이 없으면 FRULA를 출력해라

# 무조건 문자열과 같아야 함

word = list(input())
ex_word = list(input())

result = []

for x in word:
    result.append(x)
    if len(result) < len(ex_word):
        continue
    else:
        if result[-len(ex_word):] == ex_word:
            del result[-len(ex_word):]
            
if len(result) == 0:
    print("FRULA")
else:
    print(''.join(result))
    



# 만약에 word의 길이가 0이 되면 FRULA 출력하기
# 무지성 추가 후 같으면 빼기
