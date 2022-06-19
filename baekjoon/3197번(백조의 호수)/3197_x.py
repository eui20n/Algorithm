"""
    문제 이름 : 백조의 호수
    URL : https://www.acmicpc.net/problem/3197
    ----------------------------------------------
    <문제 설명>
    매일 물과 접촉한 호수는 녹는다(대각선은 제외)
    백조는 세로나 가로로만 이동 가능할때 며칠이 지나야 백조들이 만날 수 있는지 구해라
    백조는 무조건 2마리이다
"""
from collections import deque
import sys

R, C = map(int, sys.stdin.readline().split())
lake = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
