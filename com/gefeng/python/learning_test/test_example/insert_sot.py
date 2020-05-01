# coding=utf-8


def insert_sort(list_a, num):
    lenth = len(list_a)
    if list_a[0] > list_a[1]:
        for i in range(lenth-1):
            if num > list_a[i]:
                temp1 = num
                for j in range(i, lenth):
                    temp2 = list_a[j]
                    list_a[j] = temp1
                    temp1 = temp2
                list_a.append(temp1)
                break
        print(list_a)


if __name__ == "__main__":
    list_b = [20, 15, 11, 8, 5, 2]
    insert_sort(list_b, 10)