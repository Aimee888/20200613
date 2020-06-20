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
import multiprocessing
from PyQt5.QtCore import QProcess


# 方法一：用subprocess开启进程调用exe
def execute_exe_subprocess(exe_path, exe_param):
    folder_path, file_name = os.path.split(exe_path)
    try:
        # cwd:指定exe运行的路径
        p = subprocess.Popen(exe_path + " " + exe_param, stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd=folder_path)
    except:
        s = sys.exc_info()
        str_error = "Error '%s' happened on line %d" % (s[1], s[2].tb_lineno)
        print(str_error)
        return None

    try:
        output, errs = p.communicate(timeout=30)
    except subprocess.TimeoutExpired:
        p.kill()
        output, errs = p.communicate()

    # output = p.communicate()[0]
    # err = p.communicate()[1]
    print(p.returncode)
    if p.returncode == 0:
        print("pass")
    else:
        print("fail")


# 方法二：用PyQt5的方法QProcess开启进程调用exe
def execute_exe_qprocess(exe_path, exe_param):
    process = QProcess()
    folder_path, file_name = os.path.split(exe_path)
    # 指定exe运行的路径
    process.setWorkingDirectory(folder_path)
    param = exe_param.split(" ")
    process.start(exe_path, param)
    # 设置超时时间20s，如果a=True，说明exe执行完毕。如果a=False，说明到达超时时间，关闭exe执行进程
    a = process.waitForFinished(20000)
    output = process.readAll()  # exe的输出信息
    returncode = process.exitCode()  # exe的返回值
    print(a)
    print(output)
    print(returncode)


# 方法一：多进程方法调用
def multiprocess_test(function_target):
    current_path = os.getcwd()
    readini_abs_path = current_path + "\\" + r"EXEModule\ReadINI\readini.exe"
    rose_abs_path = current_path + "\\" + r"EXEModule\Rose\rose.exe"
    usage_abs_path = current_path + "\\" + r"EXEModule\CPUUsage\CPUUsage.exe"

    p1 = multiprocessing.Process(target=function_target, args=(readini_abs_path, ""))
    p1.start()
    p2 = multiprocessing.Process(target=function_target, args=(rose_abs_path, ""))
    p2.start()
    p3 = multiprocessing.Process(target=function_target, args=(usage_abs_path, ""))
    p3.start()

    p1.join()
    p2.join()
    p3.join()


# 方法二：多线程方法调用
def threading_test(function_target):
    current_path = os.getcwd()
    readini_abs_path = current_path + "\\" + r"EXEModule\ReadINI\readini.exe"
    rose_abs_path = current_path + "\\" + r"EXEModule\Rose\rose.exe"
    usage_abs_path = current_path + "\\" + r"EXEModule\CPUUsage\CPUUsage.exe"

    t1 = threading.Thread(target=function_target, args=(readini_abs_path, ""))
    t2 = threading.Thread(target=function_target, args=(rose_abs_path, ""))
    t3 = threading.Thread(target=function_target, args=(usage_abs_path, ""))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == '__main__':
    """
    方法一：多线程调用Subprocess开启进程执行exe
    同时调用多个exe               V
    获取exe打印数据               V
    按照先后顺序输出打印数据      X --耗时最长的exe运行完毕后一起输出
    exe中的Pause暂停              X
    
    多线程调用，因为有p.communicate()[0]的存在，会导致打印阻塞，一直等到耗时长的程序执行完才会打印消息
    详细解释：有一个close_fds的参数，如果设置close_fds=True，可以取消子进程对父进程的继承，不过Windows下，它不可以和管道
            同时使用，否则报错。python3.5以上默认close_fds为False，当开启一个subprocess，就会有一个fd开启，当exe运行完毕
            后，就会关闭fd，如果开启多个exe程序，其中exe运行完了，它的fd关掉了，但是其他exe还没运行完毕，fd还处在开启状
            态，只要有一个fd还没有关掉，p.communicate()[0]就会在阻塞状态，等待输出。所以，只有最耗时的程序运行完了，所有
            的fd也就关掉了，然后输出就一起打印出来了。
    """
    # threading_test(execute_exe_subprocess)

    """
    方法二：多线程调用QProcess开启进程执行exe
    同时调用多个exe               V
    获取exe打印数据               V
    按照先后顺序输出打印数据      V
    exe中的Pause暂停              V --exe中执行到pause会停住，直到超时时间到了，结束exe程序
    
    如果实在QTread的类下调用exe，推荐使用这种方法，如果是一般的情况，可以使用mutltiprocessing。
    """
    threading_test(execute_exe_qprocess)

    """
    方法三：多线程调用QProcess开启进程执行exe
    同时调用多个exe               V
    获取exe打印数据               V
    按照先后顺序输出打印数据      V
    exe中的Pause暂停              X
    
    若某个类继承QThread，并且和窗口有信号槽的联系，使用multiprocessing会直接报错
    """
    # multiprocess_test(execute_exe_subprocess)

    """
    方法四：多线程调用QProcess开启进程执行exe
    同时调用多个exe               V
    获取exe打印数据               V
    按照先后顺序输出打印数据      V
    exe中的Pause暂停              V --exe中执行到pause会停住，直到超时时间到了，结束exe程序
    
    若某个类继承QThread，并且和窗口有信号槽的联系，使用multiprocessing会直接报错
    """
    # multiprocess_test(execute_exe_qprocess)
