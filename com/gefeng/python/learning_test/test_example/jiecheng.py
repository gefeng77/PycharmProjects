# coding=utf-8


def jiecheng(num):
    for i in range(1, 21):
        s = 1
        sum = 0
        for j in range(1, num+1):
            s *= j
            sum += s
    print("Result is: %d" % sum)


if __name__ == "__main__":
    jiecheng(4)