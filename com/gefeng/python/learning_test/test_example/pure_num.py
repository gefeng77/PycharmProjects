# coding=utf-8
import math


def pure_num(num):
    """判断一个数字是否是素数，注意标志位的使用"""
    leap = 1
    # math.sqrt()--平方根
    k = int(math.sqrt(num))
    for i in range(2, k+1):
        if num % i == 0:
            leap = 0
            print("%d 不是素数！" % num)
            break
    if leap == 1:
        print("%d 是素数！" % num)


if __name__ == "__main__":
    pure_num(57)