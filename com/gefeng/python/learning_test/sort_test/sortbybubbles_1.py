# coding=utf-8
list_A = [3, 8, 2, 7, 5]
s = range(len(list_A))[::-1]
for i in s:
    # print(i)
    for j in range(i):
        print(str(i) + "," + str(j))
        if list_A[j] > list_A[j+1]:
            list_A[j], list_A[j+1] = list_A[j+1], list_A[j]
print(list_A)
