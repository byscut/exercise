#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 4:51 下午
# @File    : jz06.py
# @author  : Bai
# @Software: PyCharm
# jz06 : 从头到尾打印链表：输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        return l[::-1]
