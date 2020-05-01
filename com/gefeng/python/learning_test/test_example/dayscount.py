# coding=utf-8
import math


def count_days(year, month, day):
    count = 0
    for i in range(1, month+1):
        count = math.floor(i/2)*31 + math.floor((i-1)/2)*30
    if month == 9:
        count += 1
    count += day

    if month > 2:
        if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
            count -= 1
        else:
            count -= 2
    print("年, 月, 日, 总天数：", year, month, day, count)


if __name__ == '__main__':
    for j in range(1, 13):
        count_days(int(2020), int(j), int(30))
