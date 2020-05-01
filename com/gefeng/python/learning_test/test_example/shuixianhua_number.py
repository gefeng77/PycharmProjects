# coding=utf-8


def shuixianhua_num(num):
    num_copy = num
    sum = 0
    while num:
        temp = num % 10
        num = int(num / 10)
        sum += temp**3
    if sum == num_copy:
        print("水仙花数： %3d" % num_copy)


if __name__ == "__main__":
    for j in range(100, 999):
        shuixianhua_num(j)