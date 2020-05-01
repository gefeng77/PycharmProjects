# coding=utf-8


def multiple(num):
    """乘法表"""
    # for i in range(1, num+1):
    #     for j in range(1, i+1):
    #         s = i * j
    #         print("%d * %d = %-5d" % (j, i, i*j), end="")
    #     print("")

    """倒三角乘法表"""
    for i in range(num, 1, -1):
        for j in range(1, i+1):
            s = i * j
            # end=""，表示用空格间隔
            print("%d * %d = %-5d" % (j, i, i*j), end="")
        print("")


if __name__ == "__main__":
    multiple(9)