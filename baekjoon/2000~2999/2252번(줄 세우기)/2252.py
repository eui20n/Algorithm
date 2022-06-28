"""
    문제 이름 : 줄 세우기
    URL : https://www.acmicpc.net/problem/2252
    ----------------------------------------------
    <문제 설명>
    키가 작은 학생이 먼저 줄을 세우면 된다
    입력이 A B 꼴로 들어오는데 A가 B앞에 서면 된다는 뜻이다 => A -> B
    답이 여러개이고 답 중 하나만 출력하면 된다
    A와 B는 여러번 등장 가능
"""
from collections import deque

N, M = map(int, input().split())
student = [list(map(int, input().split())) for _ in range(M)]
student_cnt = [0] * (N + 1)
student_cnt[0] = False
student_height = [[] for i in range(N+1)]
start = []

for x in student:
    student_cnt[x[1]] += 1
    student_height[x[0]].append(x[1])

for x in range(1,len(student_cnt)):
    if student_cnt[x] == 0:
        start.append(x)

def topology_sort(start):
    q = deque(start)
    result = []
    while q:
        p = q.popleft()
        result.append(p)
        if len(student_height[p]) == 0:
            continue

        for x in student_height[p]:
            student_cnt[x] -= 1
            if student_cnt[x] == 0:
                q.append(x)


    return result

print(' '.join(map(str,topology_sort(start))))
# print("student: ", student)
# print("student_cnt: ", student_cnt)
# print("student_height: ", student_height)
# print("start: ",start)


