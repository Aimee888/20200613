#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200613 -> list_study.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/15 15:21
@Desc    :1. 列表的学习，增删改查
            2. 写一个九九乘法表
            列表和元组的区别：列表生成以后还可以往里面添加数据，也可以删除数据；但是元组一旦生成就不能修改。
            如果它里面只有整数、浮点数、字符串、另一个元组，就即不能添加数据，也不能删除数据，还不能修改里面数据的值。
            但是如果元组里面包含了一个列表，那么这个元组里面的列表依旧可以变化。
================================================="""


# 增
def add(my_list):
    # ====================== 增
    my_list.append(3)
    print("在末尾添加元素3: ", end="")
    print(my_list)
    my_list.insert(1, 4)
    print("在位置1插入元素4: ", end="")
    print(my_list)
    return my_list


# 删
def delete(my_list):
    # ====================== 删
    # 默认删除第一个2
    my_list.remove(2)
    print("删除出现的第一个元素2: ", end="")
    print(my_list)
    # 删除指定位置
    my_list.pop(3)
    print("删除位置3的元素: ", end="")
    print(my_list)
    my_list.pop(-1)
    print("删除末尾的元素: ", end="")
    print(my_list)
    my_list.clear()
    print("清空列表: ", end="")
    print(my_list)
    return my_list


# 改
def update(my_list):
    # ====================== 改
    my_list[0] = 8
    print("将位置0的元素改为8：", end="")
    print(my_list)
    my_list[1:2] = "python"
    print("在位置1和位置2中间的数据替换成'Python'（1） : ", end="")
    print(my_list)
    my_list[1:2] = ["python"]
    print("在位置1和位置2中间的数据替换成'Python'（2） : ", end="")
    print(my_list)
    return my_list


# 查
def find(my_list):
    # ====================== 查
    print("查询位置1的元素: ", end="")
    print(my_list[1])
    return my_list


def main():
    my_list = [0, 1, 2]
    print("当前列表为：", end="")
    print(my_list)

    my_list = add(my_list)
    my_list = delete(my_list)
    # 由于delete函数执行完后清空了列表，所以重新生成一个列表
    my_list = add(my_list)
    my_list = update(my_list)
    my_list = find(my_list)


# 九九乘法表
def nine_nine_multi():
    # 九九乘法表
    for row in range(1, 10):
        for colum in range(1, row + 1):
            print("{} * {} = {}".format(colum, row, colum*row), end="\t")
        print("")


if __name__ == '__main__':
    # main()
    nine_nine_multi()

