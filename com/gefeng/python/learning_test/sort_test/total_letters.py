# coding=utf-8
"""统计每个字母出现的次数"""
from itertools import count

list_A = ['a', 'b', 'c', 'b', 'c', 'c', 'a', 'c', 'b', 'c']
set_A = set(list_A)
print(set_A)

dict_A = {}
for i in list_A:
    dict_A[i] = list_A.count(i)
print(dict_A)

# count()在list和str的用法不一样
list_str = "abcdabacdab"
print(list_str.count('a', 0, 8))
