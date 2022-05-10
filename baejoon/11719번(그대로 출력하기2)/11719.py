# 그래도 출력하기2
while True:
    try:
        a = list(map(str,input()))
        print(''.join(a))
    except EOFError: break