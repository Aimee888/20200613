#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> function_study.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/22 9:16
@Desc    :运行结果
                第一步
                函数返回值：[100]
                第二步
                函数返回值：[100, 50]
                第三步
                函数返回值：[100]
                第四步
                函数返回值：[50]
        为什么第二步值不是[50]呢？涉及到Python底层的实现，不做深入讨论，建议用修改后的函数
        另外，"is"关键字，速度会比"=="稍微快一些
================================================="""


def default_para_without_trap(para=[], value=0):
    para.append(value)
    return para


def modified_default_para_without_trap(para=None, value=0):
    if para is None:
        para = []
    para.append(value)
    return para


if __name__ == '__main__':
    print("第一步")
    print("函数返回值：{}".format(default_para_without_trap(value=100)))
    print("第二步")
    print("函数返回值：{}".format(default_para_without_trap(value=50)))

    print("第三步")
    print("函数返回值：{}".format(modified_default_para_without_trap(value=100)))
    print("第四步")
    print("函数返回值：{}".format(modified_default_para_without_trap(value=50)))

