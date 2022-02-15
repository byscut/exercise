#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 11:08 上午
# @File    : version_compare.py
# @author  : Bai
# @Software: PyCharm
import re


def versionCompare(v1, v2):
    v1_check = re.match("\d+(\.\d+){0,2}", v1)
    v2_check = re.match("\d+(\.\d+){0,2}", v2)
    if v1_check is None or v2_check is None or v1_check.group() != v1 or v2_check.group() != v2:
        raise Exception("版本号格式不对，正确的应该是x.x.x,只能有3段")
    v1_list = v1.split(".")
    v2_list = v2.split(".")
    v1_len = len(v1_list)
    v2_len = len(v2_list)
    if v1_len > v2_len:
        for i in range(v1_len - v2_len):
            v2_list.append("0")
    elif v2_len > v1_len:
        for i in range(v2_len - v1_len):
            v1_list.append("0")
    else:
        pass
    for i in range(len(v1_list)):
        if int(v1_list[i]) > int(v2_list[i]):
            return 1
        if int(v1_list[i]) < int(v2_list[i]):
            return -1
    return 0


# 测试用例
if __name__ == '__main__':

    print(versionCompare(v1="2.11", v2="2.2"))
    print(versionCompare(v1="1.0.5", v2="4.0.1"))
    print(versionCompare(v1="1.0.1", v2="1.0.1"))
    print(versionCompare(v1="1.0.2", v2="1.0.1"))
    print(versionCompare(v1="1.0.1", v2="1.0.2"))
    print(versionCompare(v1="1.0.11", v2="1.0.2"))

    match_result = [
        {"effect_id": "33131", "version": "2.2.1"},
        {"effect_id": "4411", "version": "2.11.0"},
        {"effect_id": "12313", "version": "2.2.1"},
        {"effect_id": "51251", "version": "1.0"},
    ]
    import functools

    res = sorted(match_result, key=functools.cmp_to_key(lambda x, y: versionCompare(x.get('version', '0.0'), y.get('version', '0.0'))), reverse=True)
    print(res)