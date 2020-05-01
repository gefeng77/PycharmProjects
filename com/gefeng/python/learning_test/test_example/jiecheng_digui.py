# coding=utf-8


def digui(num):
    if num == 1:
        s = 1
    # return s
    else:
        s = num * digui(num-1)
    print("%d" % s)
    return s


if __name__ == "__main__":
   digui(5)
