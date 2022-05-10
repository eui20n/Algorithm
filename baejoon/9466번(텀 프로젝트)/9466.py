# 텀 프로젝트
# 프토젝트 팀원 수에는 제한이 없다 -> 만약 모든 학생들이 동일한 팀일 경우 팀은 1개만 있게 되는 거다
# 학생들은 같이 프로젝트 하고 싶은 사람(한사람만) 선택할 수 있다, 만약 혼자하고 싶으면 자기 자신을 선택해도 된다
# 학생들이(s1,s2,...,sr)이라 할때, r = 1이고 s1이 s1을 선택하는 경우나 s1이 s2를 선택하고 s2가 s3를 선택하고..... sr이 s1을 선택하는 경우 한 팀이 될 수 있다
# 선택을 받지 못하는 학생의 수를 출력해라

# 종료조건 잘 생각하기
# 1 -> 2 -> 3 -> 2 ==> 1은 팀이 없음, 이 경우 구현하기
def term_project(n,start,student):
    '''팀을 나눠주는 함수'''
    if start == student[start]:
        result[start] = 'A' # alone의 약자로 A -> 혼자 팀하는 사람
        return
    
    if student[start] not in team:
        team.add(student[start])
        
    if start in team:
        result[start] = 'T'
        return
    
    term_project(n,student[start],student)
    
    if result[student[start]] == 'A' or result[student[start]] == 'x':
        result[start] = 'x' # 팀이 없는 사람
    
    
    
    
    
T = int(input())
for i in range(T):
    n = int(input())
    student = list(map(int,input().split()))
    student = [0] + student
    result = [0]*(n+1)
    team = set([])
    for x in range(1,n+1):
        term_project(n,x,student) # 반복문 돌려서 1 부분을 계속 바꿀것
            
    
# a -> b -> c -> d -> e -> b 이런경우 b,c,d,e는 팀이고 a는 팀이 없는 사람이 된다
# 만약에 혼자하고 싶은 사람이랑 같이 하고 싶은 사람이 있으면 이 사람은 팀이 없는 사람이 된다
# 또한 위에서 저 사람을 선택한 사람도 역시 팀이 없는 사람이 된
# ==> 결국 한 바퀴 돌아서 자기 자신이 나와야 한 팀
# 반례 3 3 1 2 1 -> 출력이 3이 나와야 함
# 다시 생각해보기
# 7(4) -> 6(7) -> 4(6) -> 7(4)
# 3(1) -> 3(3) -> 3(3)