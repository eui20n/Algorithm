# 암호만들기
# 암호는 서로다른 알파벳 소문자들로 구성되며, 최소 한 개의 모음과 최소 두 개의 자음으로 구성되어 이싸고 알려져 있다
# 암호는 사전순으로 정렬이 되어있음

L,C = map(int,input().split())
password = list(map(str,input().split()))
result = []
# 모음의 개수룰 세고 길이를 뺏을때 그 길이가 2이상이여야함

def make(word,L):
    if len(word) == L:
        count = 0
        word.sort()
        for x in word:
            if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
                count +=1
        if len(word) - count >= 2 and count >= 1:
            if ''.join(word) in result:
                return 1
            result.append(''.join(word))
        return 1
    
    for x in word:
        new_list = set(word) - set([x])
        make(list(new_list),L)
            
make(password,L)
result.sort()
for x in result:
    print(x)
        
    
    
    