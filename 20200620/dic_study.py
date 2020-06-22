#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> dic_study.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/20 17:04
@Desc    :字典value的获取方式三种：dic[key], dic.get(key), dic.get(key, "key不存在时返回的值")
        1. dic[key]方式，如果key不存在会报错keyError
        2. dic.get(key), 如果key不存在会返回None，不报错
        3. dic.get(key, "aaa")，如果key不存在会返回aaa， 不报错
================================================="""


if __name__ == '__main__':
    dic = {"a": 1, "b": 2, "c": 3, "d": 4}

    # 方法一
    a = dic.get("a")
    print(a)

    # 方法二
    b = dic["b"]
    print(b)

    # 方法三
    # 在找不到key时，返回333
    c = dic.get("e", "333")
    print(c)

    d = dic.get("e")
    print(d)

    # e = dic["e"]
    # print(e)

    dic["e"] = "mmm"
    print(dic)

    dic["a"] = "aaaa"
    print(dic)

