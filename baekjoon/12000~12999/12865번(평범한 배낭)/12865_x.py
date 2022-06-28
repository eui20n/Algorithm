# 평범한 배낭
# 배낭에 물건을 가치가 높은 물건을 최대한 많이 담는 문제
# 입력은 첫줄 N에 물품의 수와 배냥이 버틸 수 있는 무게 K
# 두번째 줄부터는 그 물품에 대한 무게와 가치가 주어진다
# 출력은 배낭에 넣을 수 있는 가치의 최대값을 구해라

N,K = map(int,input().split())
bp = []
for _ in range(N):
    a,b = map(int,input().split())
    bp.append([a,b])

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]




