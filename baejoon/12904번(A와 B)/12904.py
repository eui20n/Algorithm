# A와 B
# 아래의 연산을 이용하여 A 를 B로 만들기
# 문자열의 뒤에 A를 추가한다
# 문자열을 뒤집고 뒤에 B를 추가한다

A = input()
B = input()

num = [] # 결과를 담아줄 리스트 생성

def make(A,B):
    # 만약에 A와 B가 같다면 num 리스트에 아무거나 저장해서 반환해줌
    if A == B:
        return num.append(1)
    # 만약 A가 B보가 길다면 그냥 종료 시킴 -> 문제의 조건에 위배됨
    if len(A) >= len(B):
        return
    
    # 문제에서는 A로 B를 만들기 인데 반대로 생각해서 시간을 줄임 -> B로 A를 만들기
    # 만약 B의 마지막 원소가 'A'면 make(A,B[:len(B)-1])을 해줌 -> B에서 마지막 원소를 빼줌
    if B[len(B)-1] == 'A':
        make(A,B[:len(B)-1])
    # 만약에 B의 마지막 원소가 'B'면 make(A,B[:len(B)-1][::-1])을 해줌 -> B에서 마지막 원소를 빼주고 뒤집어줌
    if B[len(B)-1] == 'B':
        make(A,B[:len(B)-1][::-1])
    # 만약에 위의 두 조건문에 걸리지 않았다면 만들 수 없다는 소리니까 종료 시킴
    return

# 함수 호출 하고 num의 길이가 1 이상이면 1을 출력 아니면 0 출력
make(A,B)
if len(num) >= 1:
    print(1)
else:
    print(0)
    
# 재귀를 활용해서 문제를 해결함