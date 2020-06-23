#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> download_story.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/23 9:40
@Desc    :正则爬取小说《动物农场》的所有章节
================================================="""
import requests
import re
import os
import time
from multiprocessing.dummy import Pool


def save_file(chapter, arcticle):
    os.makedirs('动物农场', exist_ok=True)  # 判断文件夹是否存在，不存在就创建，存在就什么都不做
    # 此处用join比较好，因为linux和windows下面路径的斜杠方向不一样.linux: "/", windows: "\"，如果使用join，会自动匹配分隔符
    file_path = os.path.join('动物农场', chapter + '.txt')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(arcticle)


def get_article(html):
    chapter_name = re.search('size="4">(.*?)<', html, re.S).group(1)
    text_block = re.search('<p.*?>(.*?)</p>', html, re.S).group(1)
    text_block = text_block.replace('<br />', '')
    return chapter_name, text_block


def get_toc(html):
    toc_url_list = []
    toc_block = re.findall('正文(.*?)</tbody>', html, re.S)[0]
    toc_url = re.findall('href="(.*?)"', toc_block, re.S)
    for url in toc_url:
        toc_url_list.append(url)
    return toc_url_list


def thread_start(chapter_url):
    chapter_html = requests.get(chapter_url).content.decode("gbk")
    chapter, arcticle = get_article(chapter_html)
    save_file(chapter, arcticle)


def main():
    start = time.time()
    url_main = "http://www.kanunu8.com/book3/6879"
    html = requests.get(url_main).content.decode("gbk")
    toc_url_list = get_toc(html)
    chapter_url_list = []
    for toc_url in toc_url_list:
        add_list = [url_main, toc_url]
        chapter_url = "/".join(add_list)
        chapter_url_list.append(chapter_url)

    # 创建5个线程
    pool = Pool(5)
    # 开启线程，thread_start是函数名，chapter_url_list是参数列表，每一个元素就是传入函数的所有参数
    pool.map(thread_start, chapter_url_list)
    end = time.time()
    print(f"5线程循环访问小说，耗时：{end-start}")


if __name__ == '__main__':
    main()
