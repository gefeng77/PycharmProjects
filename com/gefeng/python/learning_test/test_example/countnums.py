# coding=utf-8
import math


def countnums(num):
    list_a = []
    leap = True
    while leap:
        if num != 0:
            a = num % 10
            num -= a
            num /= 10
            list_a.append(a)
        else:
            leap = False
    for i in range(0, len(list_a)):
        print(list_a[i])


if __name__ == "__main__":
    countnums(63571)

