"""
    문제 이름 : 텀 프로젝트
    URL : https://www.acmicpc.net/problem/9466
    ----------------------------------------------
    <문제 설명>
    1 -> 2 -> 3 -> 4 -> 1 로 가는 경우 같은 팀
    만약 1 -> 2 -> 3 -> 4 -> 2 로 가면 1은 같은 팀이 아님
    여기서 팀이 아닌 사람이 몇명 인지 구하면 됨
    자기 자신과 팀을 해도 됨
"""
from collections import deque


def topological_sorting(student_cnt, student):
    zero_index = []
    for x in range(1, len(student_cnt)):
        if student_cnt[x] == 0:
            zero_index.append(x)

    q = deque(zero_index)
    cnt = 0
    while q:
        current_loc = q.popleft()
        next_loc = student[current_loc]

        cnt += 1

        student_cnt[next_loc] -= 1
        if student_cnt[next_loc] == 0:
            q.append(next_loc)

    return cnt


T = int(input())

for _ in range(T):
    n = int(input())
    student = list(map(int, input().split()))
    student = [0] + student
    student_cnt = [0] * len(student)

    for x in range(1, len(student)):
        student_cnt[student[x]] += 1

    print(topological_sorting(student_cnt, student))

# 위상정렬을 이용해서 풀이함
