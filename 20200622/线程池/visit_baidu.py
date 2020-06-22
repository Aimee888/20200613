#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> visit_baidu.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/22 19:44
@Desc    :单线程循环访问100次百度首页，耗时：64.70974159240723
            5线程循环访问100次百度首页，耗时：11.157011985778809
================================================="""
import time
import requests
from multiprocessing.dummy import Pool


def query(url):
    requests.get(url)


def singal_thread_visit(url):
    # 单线程访问
    start = time.time()
    for i in range(100):
        query(url)
    end = time.time()
    print(f"单线程循环访问100次百度首页，耗时：{end-start}")


def five_thread_visit(url):
    # 5个线程访问
    start = time.time()
    url_list = []
    for i in range(100):
        url_list.append(url)

    pool = Pool(5)
    pool.map(query, url_list)
    end = time.time()
    print(f"5线程循环访问100次百度首页，耗时：{end-start}")


if __name__ == '__main__':
    singal_thread_visit("https://www.baidu.com")
    five_thread_visit("https://www.baidu.com")

