# coding=utf-8


def count_peaches(num):
    x2 = 1
    x1 = 0
    for i in range(10, 0, -1):
        x1 = (x2 + 1) * 2
        print("%d天的桃子数是：%d" % (i, x2))
        x2 = x1


if __name__ == "__main__":
    count_peaches(10)
