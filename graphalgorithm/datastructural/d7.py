#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/26 13:47
# @File    : d7.py
# @Author  : Richard Yang

'''剑指 Offer 35. 复杂链表的复制
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

自定义的链表没有实现这个功能，只能尝试大致方法
'''


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head:
            return []
        
        res = []
        while head:
            temp = []
            temp.append(head.val)
            temp.append(head.random)
            head = head.next
            res.append(temp)
        return res


if __name__ == "__main__":
    pass
