# A와 B
# 아래의 연산을 이용하여 A 를 B로 만들기
# 문자열의 뒤에 A를 추가한다 -> 문자열의 뒤에 있는 A를 제거 한다(반대)
# 문자열에 B를 추가하고 뒤집는다 -> 문자열을 뒤집고 문자열 뒤에 있는 B를 제거한다
# 재귀로 해보기

A = input()
B = input()

result = []
        
def make(A,B):
    if len(B) < 1:
        return 0
    if A == B:
        result.append(1)
        return 1
    if B[len(B)-1] == 'A':
        make(A,B[:len(B)-1])
    if B[::-1][len(B)-1] == 'B':
        make(A,B[::-1][:len(B)-1])
    if len(B) < len(A):
        return 0
    return 0

make(A,B)
if len(result) >= 1:
    print(1)
else:
    print(0)    
