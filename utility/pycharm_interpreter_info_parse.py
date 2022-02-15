#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 3:04 下午
# @File    : interpreter_info_parse.py
# @author  : Bai
# @Software: PyCharm
import os


def parse_project_dir(path):
    project_dir = os.listdir(path)
    print(project_dir)

    inter_list = []

    for project in project_dir:
        file_path = path + "{}/.idea/{}.iml".format(project, project)
        if not os.path.exists(file_path):
            print("文件错误，非项目目录 = {}".format(project))
        else:
            interpreter = None
            with open(file_path, 'r') as xml:
                for line in xml.readlines():
                    if "jdkName" in line:
                        interpreter = line.replace("\\n", "").replace("\n", "").strip()
            inter_list.append((project, interpreter))

    print("+++++++++++++++++++++++++++++++++++")
    for tuple_data in inter_list:
        print(tuple_data)
    print("+++++++++++++++++++++++++++++++++++")


if __name__ == '__main__':
    parse_project_dir("/Users/baiyang/git/")
    parse_project_dir("/Users/baiyang/PycharmProjects/")
