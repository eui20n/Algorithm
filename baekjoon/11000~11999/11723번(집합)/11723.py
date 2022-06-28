# 집합
# 비트마스크 가장 기초적인 문제

import sys

N = int(input())
count = 1
S = 0b0
for _ in range(N):
    a = list(sys.stdin.readline().split())
    if a[0] == 'add':
        S |= 1 << int(a[1])
    elif a[0] == 'remove':
        S &=~(1 << int(a[1]))
    elif a[0] == 'toggle':
        S ^=(1 << int(a[1]))
    elif a[0] == 'all':
        S = (1 << 21) - 1
    elif a[0] == 'empty':
        S = 0b0
    elif a[0] == 'check':
        print(1 if S &(1 << int(a[1])) != 0 else 0)