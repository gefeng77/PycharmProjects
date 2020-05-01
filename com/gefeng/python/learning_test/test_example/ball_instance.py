# coding=utf-8


def ball_instance(time):
    n = 100
    instance = 0
    for i in range(time):
        instance += n + n/2
        n = n/2
        print("%.4f" % n)
    print("%.4f" % instance)


if __name__ == "__main__":
    ball_instance(10)