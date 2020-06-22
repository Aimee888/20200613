#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> dic_re_if.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/22 9:01
@Desc    :if-elif-else繁杂有时可用dict代替
================================================="""


def dic_func(state):
    state_dict = {
        'start': 1,
        'running': 2,
        'offline': 3,
        'unknow': 4,
    }
    return state_dict.get(state, 5)


def if_func(state):
    if state == 'start':
        code = 1
    elif state == 'running':
        code = 2
    elif state == 'offline':
        code = 3
    elif state == 'unknow':
        code = 4
    else:
        code = 5
    return code


if __name__ == '__main__':
    # state_value = "start"
    state_value = "error"
    code_value = if_func(state_value)
    print(code_value)

    code_value = dic_func(state_value)
    print(code_value)

