# coding=utf-8


def zhiyinshu(num):

    print("{}=".format(num), end="")

    while num != 1:
        for i in range(2, num+1):
            if num % i == 0:
                num = int(num/i)
                if num == 1:
                    print(i)
                else:
                    print("{}*".format(i), end="")
                break


number = input("Please input a number:")
zhiyinshu(int(number))
