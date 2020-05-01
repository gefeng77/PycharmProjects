# coding=utf-8
class Person(object):
    """打印实例内容"""

    def __init__(self):
        self.name = "阿三"

# 美化类实例的打印内容，python3中用__str__，python2中用__unicode__
    # def __str__(self):
    #     return self.name

#  返回docstring里面的内容
    def __str__(self):
        return self.__doc__


if __name__ == '__main__':
    child = Person()
    print(child)