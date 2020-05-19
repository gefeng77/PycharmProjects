# coding=utf-8


def huiwen(str1):
    flag = True
    # 方法1
    # for i in range(int(len(str1)/2)):
    #     if str1[i] != str1[-i-1]:
    #         flag = False
    #         break

    # 方法2
    # if str1 != str1[::-1]:

    # 方法3
    # rev_str = reversed(str1)
    # # print(rev_str)
    # if list(str1) != list(rev_str):
    #     flag = False
    if flag:
        print("%s 是回文。" % str1)
    else:
        print("%s 不是回文。" % str1)

    # 字符串处理
    str_test = "Hello World!"
    # 输出变量的地址信息
    print(reversed(str_test))
    # 用下面这种方式会报错
    # print(str(reversed(str_test)))

    print("".join(reversed(str_test)))


if __name__ == "__main__":
    str = input("Please input a string.")
    huiwen(str)
    try:
        a = 5/0
    except ZeroDivisionError as e:
        print(e)

