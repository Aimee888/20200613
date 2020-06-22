#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> guess_number.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/22 10:03
@Desc    :猜数游戏，二分法
================================================="""
from numpy.random import randint
import math


answer_range = 1024  # 随机数范围(0, 1024)


history = {}


def try_to_guess(name, answer):
    try_num = 0
    while try_num < math.log2(answer_range):
        guess_answer = int(input('请输入一个数字：'))
        if guess_answer < answer:
            print('你输入的数字比正确答案小。')
        elif guess_answer == answer:
            print('回答正确!')
            history[name].append('成功')
            break
        else:
            print('你输入的数字比正确答案大。')
        try_num += 1
    else:
        print('猜错次数太多，失败')
        history[name].append('失败')


def default():
    pass


def start():
    user_name = input("请输入用户名：")
    history[user_name] = []
    answer_value = randint(0, answer_range)
    # print(answer_value)
    try_to_guess(user_name, answer_value)


def show_history():
    for key, value in history.items():
        print("用户：", end='')
        print(key, end='\t\t\t')
        print("记录如下：", end="")
        print(value)


if __name__ == '__main__':
    select_dict = {
        '1': show_history,
        '2': start,
        '3': exit
    }
    while True:
        select = input('1.历史记录\n2.继续游戏\n3.退出游戏\n输入数字选择：')
        select_dict.get(select, default)()
