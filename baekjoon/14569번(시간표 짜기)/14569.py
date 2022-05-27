# 시간표 짜기
# 수강신청 기간에 학생들은 비어 있는 시간에 어떤 과목을 추가로 신청할 수 있는지 궁금해 한다
# 이 궁금증을 해결해라
# 과목끼리 시간이 겹치더라도 모두 세어야 한다

N = int(input())
sch = []
for _ in range(N):
    a = list(map(int,input().split()))
    sch.append(a)
    
M = int(input())
s_sch = []
for _ in range(M):
    a = list(map(int,input().split()))
    s_sch.append(a)
    
for x in s_sch:
    count  = 0
    for y in sch:
        if set(y[1:]) & set(x[1:]) == set(y[1:]):
            count +=1
    print(count)
    
