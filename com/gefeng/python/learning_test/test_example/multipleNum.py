# coding=utf-8


def multiple_Num(num):
    if num <= 1:
        print("请输入大于1的正整数！")
    for i in range(2, num+1):
        if num % i == 0:
            num /= i
            if num == 1:
                print(i)
            else:
                print("{} *".format(i), end=" ")


if __name__ == "__main__":
    multiple_Num(80)