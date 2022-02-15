#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 2:52 下午
# @File    : jz07.py
# @author  : Akaya
# @Software: PyCharm
# jz07  : 重建二叉树：输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        in_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1 + in_index], inorder[:in_index])
        root.right = self.buildTree(preorder[1 + in_index:], inorder[in_index + 1:])
        return root
