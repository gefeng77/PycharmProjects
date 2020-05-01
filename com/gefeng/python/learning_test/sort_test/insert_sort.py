# coding=utf-8


def insert_sort(*args):
    # 将参数中元祖的值付给数组
    list_a = []
    for i in args:
        list_a.append(i)
    print(list_a)
    
    for i in range(1, len(list_a)):
        key = list_a[i]
        j = i-1
        while j >= 0 and list_a[j] > key:
            list_a[j+1] = list_a[j]
            j -= 1
        list_a[j+1] = key
    print(list_a)


if __name__ == "__main__":
    insert_sort(4, 2, 5, 8, 7, 9, 1)











