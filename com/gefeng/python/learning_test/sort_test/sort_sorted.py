# coding=utf-8
"""list对象的sort方法，sort仅针对list对象排序"""
list_str = ["Hello Linda!", "learning_test", "World", "python", "C++"]
list_str.sort(key=lambda x: len(x))
print(list_str)

list_t = [{"Linda": "85"}, {"Kevin": "100"}, {"Jessica": "98"}, {"Gabbie": "89"}, {"Vivian": "75"}]
list_t.sort(key=lambda x: list(x.values())[0])
print(list_t)

dict_A = {"Linda": "85", "Kevin": "100", "Jessica": "98", "Gabbie": "89", "Vivian": "75"}
# 以列表形式输出字典中的Key
b1 = [key for key, value in dict_A.items()]
print(b1)

# 以列表形式输出字典中的value
b2 = [value for key, value in dict_A.items()]
print(b2)

# sorted是一个单独的函数，对可迭代对象排序，不局限于list，不改变原生数据，重新生成一个新的队列

# 根据字典中value的值升序排列
b3 = sorted(dict_A.items(), key=lambda x: x[1])
print(b3)
