#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> CallEXEParaller.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/13 14:20
@Desc    :目的：可以并行调用两个或者多个EXE
================================================="""
import subprocess
import sys
import os
import threading


SECONDS_TIMEOUT = 1000


def execute_exe(exe_path, exe_param):
    folder_path, file_name = os.path.split(exe_path)
    os.chdir(folder_path)
    p = subprocess.Popen(exe_path + " " + exe_param, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        p.wait(timeout=SECONDS_TIMEOUT)
    except Exception as e:
        p.kill()
        os.chdir(current_path)
        print("===== process timeout ======")
        return None
    except:
        s = sys.exc_info()
        str_error = "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
        p.kill()
        os.chdir(current_path)
        return None
    os.chdir(current_path)
    output = p.communicate()[0]
    err = p.communicate()[1]
    print(output)
    print(p.returncode)


if __name__ == '__main__':
    current_path = os.getcwd()
    rose_abs_path = current_path + "\\" + r"EXEModule\Rose\rose.exe"
    usage_abs_path = current_path + "\\" + r"EXEModule\CPUUsage\CPUUsage.exe"
    t1 = threading.Thread(target=execute_exe, args=(rose_abs_path, ""))
    t2 = threading.Thread(target=execute_exe, args=(usage_abs_path, ""))
    t1.start()
    t2.start()
