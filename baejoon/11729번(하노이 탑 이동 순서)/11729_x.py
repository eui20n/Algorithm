# 하노이 탑 이동 순서
# 그냥 하이노탑의 이동 순서를 출력하면 됨
# 입력은 하노이 탑의 높이가 입력이 되고, 출력은 첫줄에는 이동하는 횟수와 그 다음줄에는 이동하는 순서(그 원판을 출력하는게 아니라 이동하는 곳)를 출력하면 됨

N = int(input())
hanoi_top = [[] for _ in range(3)]
hanoi_top[0] = list(range(1,N+1))

def hanoi(N):
    if len(hanoi_top[2]) == N:
        return
    else:
        if len(hanoi_top[2]) == 0:
            hanoi_top
            
# 하노이탑의 이동 순서(규칙)를 정확히 알고 풀어야함
    