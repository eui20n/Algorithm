# 동전 0
# 첫줄에는 동전의 종류 N과 금액 M이 주어짐
# 그 다음줄 부터는 동전들이 한줄씩 입력이 됨
# 이 때 금액에 필요한 동전의 최솟값을 출력하면 됨

N,K = map(int,input().split())
kind = []
for _ in range(N):
    a = int(input())
    kind.append(a)
    
kind.reverse()
count = 0

for x in kind:
    while K >= x:
        K -=x
        count +=1
print(count)
