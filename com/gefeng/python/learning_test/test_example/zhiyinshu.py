# coding=utf-8
import math


def zhiyinsu(num):
    if num <= 0:
        print("请输入正整数")
    num_copy = num
    list_a = []
    i = 2
    result = 1
    # while num > 1:
    #     # 求因子
    #     for k in range(2, i+1):
    #         if num % k == 0:
    #             # 判断因子是否为素数
    #             for j in range(2, int(math.sqrt(k))+1):
    #                 if k % j == 0:
    #                     break
    #             else:
    #                 num /= k
    #                 list_a.append(k)
    #                 result *= k
    #                 if result == num_copy:
    #                     break
    #         if result == num_copy:
    #             break
    #     i += 1
    while num > 1:
        for index in range(2, int(num+1)):
            if num % index == 0:
                num /= index
                if num == 1:
                    print(index)
                else:  # index 一定是素数
                    print("{} *".format(index), end=" ")
                break

    # print(list_a)


if __name__ == "__main__":
    zhiyinsu(36)



