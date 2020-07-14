#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> red_packets.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/29 14:56
@Desc    :使用pygame播放音乐
================================================="""
import pygame
import time


# 声音提示
def voice():
    # 初始化工具包
    pygame.mixer.init()
    pygame.mixer.music.load("dayu.mp3")
    pygame.mixer.music.play()
    time.sleep(10)


def main():
    voice()


if __name__ == '__main__':
    main()
