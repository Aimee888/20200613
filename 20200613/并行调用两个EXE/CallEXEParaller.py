#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> CallEXEParaller.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/13 14:20
@Desc    :目的：可以并行调用两个或者多个EXE
        方法一：多进程方法调用，完美实现
        方法二：多线程调用，因为有p.communicate()[0]的存在，会导致打印阻塞，一直等到耗时长的程序执行完才会打印消息
================================================="""
import subprocess
import sys
import os
import threading
import multiprocessing


def execute_exe(exe_path, exe_param):
    print("aaa")
    folder_path, file_name = os.path.split(exe_path)
    try:
        p = subprocess.Popen(exe_path + " " + exe_param, stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd=folder_path)
    except:
        s = sys.exc_info()
        str_error = "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
        print(str_error)
        return None
    output = p.communicate()[0]
    err = p.communicate()[1]
    print(output)
    print(p.returncode)
    if p.returncode == 0:
        print("pass")
    else:
        print("fail")


# 方法一：多进程方法调用
def multiprocess_test():
    current_path = os.getcwd()
    readini_abs_path = current_path + "\\" + r"EXEModule\ReadINI\readini.exe"
    rose_abs_path = current_path + "\\" + r"EXEModule\Rose\rose.exe"
    usage_abs_path = current_path + "\\" + r"EXEModule\CPUUsage\CPUUsage.exe"

    p1 = multiprocessing.Process(target=execute_exe, args=(readini_abs_path, ""))
    p1.start()
    p2 = multiprocessing.Process(target=execute_exe, args=(rose_abs_path, ""))
    p2.start()
    p3 = multiprocessing.Process(target=execute_exe, args=(usage_abs_path, ""))
    p3.start()

    p1.join()
    p2.join()
    p3.join()


# 方法二：多线程方法调用
def threading_test():
    current_path = os.getcwd()
    readini_abs_path = current_path + "\\" + r"EXEModule\ReadINI\readini.exe"
    rose_abs_path = current_path + "\\" + r"EXEModule\Rose\rose.exe"
    usage_abs_path = current_path + "\\" + r"EXEModule\CPUUsage\CPUUsage.exe"

    t1 = threading.Thread(target=execute_exe, args=(readini_abs_path, ""))
    t2 = threading.Thread(target=execute_exe, args=(rose_abs_path, ""))
    t3 = threading.Thread(target=execute_exe, args=(usage_abs_path, ""))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == '__main__':
    # threading_test()
    multiprocess_test()
