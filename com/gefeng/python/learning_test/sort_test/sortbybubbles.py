# coding:utf-8
list_A = [3, 8, 2, 7, 5]
# list_A.sort()
print(list_A)

# range(start, end, step)函数生成一个列表，可用于for循环
for i in range(len(list_A)-1):
    # print(i)
    for j in range(i+1, len(list_A)):
        # print(str(i) + ", " + str(j))
        if list_A[i] > list_A[j]:
            list_A[i], list_A[j] = list_A[j], list_A[i]

print(list_A)

# 对列表进行反转/倒序
# list_A.reverse()
list_A.sort(reverse=True)
print(list_A)
# sorted返回排序后的新对象，原对象保持不变
# print(sorted(list_A))
# print(list_A)



