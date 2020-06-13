#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> three_line_code.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/13 16:26
@Desc    :链接: https://www.cnblogs.com/shann001/p/13114293.html
================================================="""
"""
错误分析代码：
    lambda x: i * x函数：
    def func(x):
        return i * x
        
    multipliers()函数：
    def multipliers():
        res_list = []
        for i in range(4):
            res = func(x)
            res_list.append(res)
        return res_list
    
    i = 0 --> res = 0;
    i = 1 --> res = x
    i = 2 --> res = 2x
    i = 3 --> res = 3x
    res_list = [0, x, 2x, 3x]
        
    m(2) for m in res_list函数:
    def main():
        result_list = []
        for m in res_list:
            result = m(2)
            result_list.append(result)
        return result_list
    m = 0 --> m(2) = 0
    m = x --> m(2) = 2
    m = 2x --> m(2) = 4
    m = 3x --> m(2) = 6
    
正确分析代码：
    上面分析看起来很对，那么问题在哪里，在于调用multipliers函数时，并没有执行func(x)函数，只是把func(x)的地址存在列表中
    所以res_list实际上是[fun(x), fun(x), fun(x), fun(x)], 真正调用func(x)函数时在执行m(2)时，当把2传进func(x)的时候，
    由于func(x)是i * x，此时x是2，结果就是2*i，func(x)中不知道i是多少，所以会去上一层寻找，然而此时上层函数早已经循环完，
    此时i的值已经是3了，所以结果是[6, 6, 6, 6]
    
"""


def multipliers():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in multipliers()])
