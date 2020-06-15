#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> readini.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/15 9:34
@Desc    :
================================================="""
import configparser
import time
import os


if __name__ == '__main__':
    conf = configparser.ConfigParser()
    print(os.getcwd())
    conf.read("testini.ini")
    name = conf.get("TEST", "name")
    print("name =", name)

    time.sleep(3)
    conf1 = configparser.ConfigParser()
    conf1.add_section("SECTION")
    conf1.set("SECTION", "name", name)
    conf1.write(open("test1.ini", "w"))
