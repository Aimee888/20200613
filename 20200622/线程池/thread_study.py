#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> thread_study.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/22 19:33
@Desc    :这个例子不涉及I/O操作，所以在Python GIL的影响下，使用三个线程并不会使代码的运行时间小于单线程的运行时间
================================================="""
from multiprocessing.dummy import Pool


def calc_power2(num):
    return num * num


def calc_power1():
    for i in range(10):
        print(i * i)


if __name__ == '__main__':
    # calc_power1()
    # 初始化3个线程的线程池
    pool = Pool(3)
    origin_num = [x for x in range(10)]
    result = pool.map(calc_power2, origin_num)
    print(f"计算0-9的平方分别为：{result}")
