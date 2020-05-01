# coding=utf-8
import time


def fib_list(n):
    """方法一："""
    # if n == 1 or n == 2:
    #     return 1
    # for i in range(n+1):
    #     return fib_list(n-1) + fib_list(n-2)

    """方法二"""
    a = 1
    b = 1
    for i in range(n-1):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    number = 8
    for j in range(1, number+1):
        print(fib_list(j))
        t = time.localtime()
    print(time.strftime("%Y-%m-%d %H:%M:%S", t))