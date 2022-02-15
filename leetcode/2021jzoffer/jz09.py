#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 3:06 下午
# @File    : jz09.py
# @author  : Akaya
# @Software: PyCharm
# jz09  : 两个栈实现队列：用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead，
# 分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )


class CQueue:
    def __init__(self):
        self.insert_stack = []
        self.pop_stack = []

    def appendTail(self, value: int) -> None:
        self.insert_stack.append(value)

    def deleteHead(self) -> int:
        if self.pop_stack:
            return self.pop_stack.pop()
        if not self.insert_stack:
            return -1
        while self.insert_stack:
            self.pop_stack.append(self.insert_stack.pop())
        return self.pop_stack.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
