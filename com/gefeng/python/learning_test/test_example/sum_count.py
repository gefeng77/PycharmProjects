# coding=utf-8
from functools import reduce


def sum_count(num1, num2):
    total = 0
    # a = num1
    # for i in range(num2):
    #     total += a
    #     a *= 10
    #     a += num1
    # print(total)
    Sn = []
    total = 0
    Tn = 0
    for i in range(num2):
        Tn += num1
        num1 *= 10
        Sn.append(Tn)
        print(Tn)
    Sn = reduce(lambda x, y: x + y, Sn)
    print(Sn)


if __name__ == "__main__":
    sum_count(6, 8)


