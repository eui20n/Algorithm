num = input()


def add_cycle():
    """ 더하기 사이클 """
    cycle_num = num

    cnt = 0

    while True:
        next_num = 0

        for x in range(len(cycle_num)):
            next_num += int(cycle_num[x])

        cycle_num = cycle_num[-1] + str(next_num)[-1]
        cnt += 1

        if int(cycle_num) == int(num):
            break

    return cnt


print(add_cycle())
