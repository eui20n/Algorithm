# 별 찍기 - 10
# 3의 거듭 제곱인 N이 있다
# 이 N은 N x N 의 정사각형을 이루고 있다
# 이 정사각형은
# ***
# * *
# *** 과 같은 모양이다
# 입력 N이 주어졌을때 위의 모양과 같은 *을 출력하라

N = int(input())

def point_star(N,list = [['*','*','*'],['*',' ','*'],['*','*','*']]):
    if N / 3 == 1:
        return list
    a = list
    return point_star(N/3,list = [[a,a,a],[a,' ',a],[a,a,a]])



