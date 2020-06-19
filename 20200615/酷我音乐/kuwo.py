#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> kuwo.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/15 14:10
@Desc    :以周深为例，下载一个页面的歌曲
================================================="""
import requests


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    'Cookie': "_ga=GA1.2.778263850.1591773087; _gid=GA1.2.1610741771.1591773087; _gat=1; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1591773087; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1591773087; kw_token=1NO4DT7T63E",
    'csrf': "1NO4DT7T63E",
    'Referer': "http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%B7%B1"
}


def get_music(rid, name):
    url = "http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1587429921873&reqId=617f0321-8369-11ea-80b3-bbd056ce88a1".format(rid)
    data = requests.get(url, headers=headers).json()
    music_url = data["url"]
    result = requests.get(music_url).content
    with open("./music/{}.mp3".format(name), "wb") as f:
        f.write(result)
    print(name, "下载完毕哦")


def main():
    url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=30&reqId=615ae920-2d21-11ea-b560-73e04c9f8018".format("毛不易", 1)
    html = requests.get(url, headers=headers).json()
    data = html["data"]["list"]
    for song in data:
        rid = song["rid"]
        name = song["name"]
        get_music(rid, name)


if __name__ == '__main__':
    get_music(54961454, "梅香如故")
    # main()
