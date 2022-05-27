#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 4:35 下午
# @File    : test_munch.py
# @author  : Bai
# @Software: PyCharm
# munch库
from munch import *

# 创建新的字典，有两种方法
# 1、新建字典1
demo = Munch(name='james', age='20')
demo2 = Munch(names='kobe', ages='40')
print(demo, demo2)
print(demo.name)  # james  取值的时候可以像orm一样直接提取, 就不需要用get，或者 ['name']
print(demo.get('name'), demo2['names'])  # 这样操作也是支持的

# 2、新建字典2
demo3 = Munch()
demo3.name = 'ad'
demo3.ages = 26
print(demo3)

# 3、修改元素
demo3.name = 'morix'
print(demo3)  # 直接就可以修改

# 4、 删除元素
demo3.pop('name')  # 第一种删除
print(demo3)
del demo3["ages"]  # 第二种删除
print(demo3)

# 5、多字典合并，或者增加单个值
demo.update(demo2)  # 输出为none，
print(demo)  # 得到一个新得munch对象
# 或者
demo.update({'ponies': 'are prettty!'}, hello=42)  # 得到一个新得munch对象
# 或者
ss = Munch({**demo, **demo2})
print(ss)  # 得到一个新的munch对象

# 6、 一个字典里面包含多个对象，并可以取出
demo = Munch(name='james', age='20', na=[1, 2, 3], demo_dict=Munch(new='test'))
print(demo.na)  # 取出可以循环的列表
print(demo.demo_dict.new)  # 链式调用

# 1、 像字典一样取出所有的key
demo = Munch(name='james', age='20', na=[1, 2, 3], demo_dict=Munch(new='test'))
print(demo.keys())  # dict_keys(['name', 'age', 'na', 'demo_dict'])

# 2、 取出所有的value
print(demo.values())

# 3、key和value 一起取出
ss = [(k, demo[k]) for k in demo]  # 第一种方法
for k, v in demo.items():  # 第二种方法
    print(k, v)

# 4、字典解构
demo2 = Munch(knights='lbj', ni='lakes')
ss = "The {knights} who say {ni}!".format(**demo2)

# 5、当键值对不符合要求的时候，需要使用get方法
print(demo2.get('hao', '0'))  # hao 不存在demo2的键值对里面, 会返回0，如果直接 demo2.hao, 会爆 AttributeError: hao 的错误

# 或者可以设定返回的默认值
demo2 = DefaultMunch('-', name='lbj')
print(demo2.hao)  # 返回设定好的 '-'

# 或者可以设定返回一个工厂函数（列表，元组，字典）
demo2 = DefaultFactoryMunch(list, name='lbj')
print(demo2.hao)  # 返回 []
print(demo2)  # 查看munch对象的时候会看到结构为 DefaultFactoryMunch(list, {'name': 'lbj', 'hao': []})
