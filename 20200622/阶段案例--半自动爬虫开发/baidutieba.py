#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> baidutieba.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/22 11:17
@Desc    :爬取百度贴吧刺客信条其中一个帖子的用户名，帖子内容， 发帖时间
            用正则匹配分别抓取用户名，内容，时间，在写入CSV文件
            弊端：如果不是一一对应关系，会产生错误
================================================="""
import re
import csv


def main():
    with open('source.txt', 'r', encoding='utf-8') as f:
        source = f.read()

    # re.S表示匹配忽略空行
    result_list = []
    username_list = re.findall('username="(.*?)"', source, re.S)
    content_list = re.findall('j_d_post_content ".*?>(.*?)<', source, re.S)
    reply_time_list = re.findall('<span class="tail-info">(2020.*?)</span>', source, re.S)

    for i in range(len(username_list)):
        result = {
            'username': username_list[i],
            'content': content_list[i],
            'reply_time': reply_time_list[i]
        }
        result_list.append(result)

    # with open('tieba.csv', 'w', newline='', encoding='gbk') as f:
    with open('tieba.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['username', 'content', 'reply_time'])
        writer.writeheader()
        writer.writerows(result_list)


if __name__ == '__main__':
    main()
