"""
    문제 이름 : 소풍
    URL : https://www.acmicpc.net/problem/2026
    ----------------------------------------------
    <문제 설명>
    1부터 N까지 번호가 붙은 학생들중 K명의 학생들을 소풍에 보내려고 한다. 그런데 소풍갈 사람은 모두 친구 사이다.
    친구 정보가 주어질 때, 소풍을 가게될 K명을 구해라
    만약 K명의 친구 관계인 학생들이 존재하지 않는다면 -1을 출력
    그 외에는 K개의 출에 학생들의 번호를 증가하는 순서로 한 줄에 한 개씩 출력
    만약에 그러한 경우게 여러개라면 첫 번째 학생의 번호가 제일 작은 것을 출력하고, 그게 여러개라면 두 번째 ... 이런식으로 출력하기
"""
K, N, F = map(int, input().split())
friend_info = [[] for _ in range(N + 1)]
for _ in range(F):
    a, b = map(int, input().split())
    friend_info[a].append(b)
    friend_info[b].append(a)
result = []
end_con = False


def show_arr(arr):
    """ arr를 보여주는 함수 """
    print(*arr, sep='\n')


def sort_arr():
    """ friend_info를 정렬해주는 함수 """
    for x in range(1, len(friend_info)):
        friend_info[x] = sorted(friend_info[x])


def picnic_student(num, friend, visited):
    """ 피크닉 가는 학생을 구해주는 함수 """
    global end_con
    global result
    if end_con:
        return

    if len(friend_info[num]) < K - 1:
        return

    if len(friend) == K:
        end_con = True
        result += friend
        return

    if len(friend) != 0:
        for x in friend:
            if x not in friend_info[num]:
                return

    for x in friend_info[num]:
        if not visited & (1 << x):

            friend.append(num)
            visited |= (1 << x)

            picnic_student(x, friend, visited)
            if end_con:
                return

            visited &= ~(1 << x)
            friend.pop()


def main():
    """ 함수를 실행 시켜줄 함수 """
    global result
    sort_arr()
    student = [x for x in range(1, N + 1)]

    for x in student:
        if len(friend_info[x]) < K - 1:
            continue

        visited = 0
        picnic_student(x, [], visited)
        if len(result) == K:
            break

    if len(result) == 0:
        print(-1)
    else:
        show_arr(result)


main()


"""
        핵심정리
    1. 그냥 평범한 백트래킹
    2. 집합은 정렬이 자동으로 되지 않음 => 당연한거긴 한테, 지식 습득
"""
