#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> baidutieba1.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/22 14:27
@Desc    :先获取每一层楼的信息，在分别在每一层楼的信息中提取用户名，内容，时间。
================================================="""
import re
import csv


def main():
    with open('source.txt', 'r', encoding='utf-8') as f:
        source = f.read()

    result_list = []

    # re.S表示匹配忽略空行
    every_reply = re.findall('l_post l_post_bright j_l_post clearfix.."(.*?)p_props_tail props_appraise_wrap',
                             source, re.S)

    for each in every_reply:
        result = {}
        result['username'] = re.findall('username="(.*?)"', each, re.S)[0]
        result['content'] = re.findall('j_d_post_content ".*?>(.*?)<', each, re.S)[0].replace('            ', '')
        result['reply_time'] = re.findall('<span class="tail-info">(2020.*?)</span>', each, re.S)[0]
        result_list.append(result)

    # with open('tieba.csv', 'w', newline='', encoding='utf-8') as f:
    with open('tieba.csv', 'w', newline='', encoding='gbk') as f:
        writer = csv.DictWriter(f, fieldnames=['username', 'content', 'reply_time'])
        writer.writeheader()
        writer.writerows(result_list)


if __name__ == '__main__':
    main()
