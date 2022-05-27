# 제로
# 0이 있으면 앞에 있는 숫자 제거하기

T = int(input())
num = []
for _ in range(T):
    a = int(input())
    if a == 0:
        num.pop()
        continue

    if a != 0:
        num.append(a)

print(sum(num))

