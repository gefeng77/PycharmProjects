# coding=utf-8


def huiwen(str1):
    flag = True
    for i in range(int(len(str1)/2)):
        if str1[i] != str1[-i-1]:
            flag = False
            break
    if flag:
        print("%s 是回文。" % str1)
    else:
        print("%s 不是回文。" % str1)


if __name__ == "__main__":
    huiwen("abcdecba")

