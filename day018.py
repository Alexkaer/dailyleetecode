"""
地址：https://leetcode-cn.com/problems/reverse-linked-list/

描述：
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL Output: 5->4->3->2->1->NULL Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

思路：
这个就是常规操作了，使用一个变量记录前驱pre，一个变量记录后继next.

不断更新current.next = pre 就好了

关键点：
链表的基本操作（交换）
虚拟节点dummy 简化操作
注意更新current和pre的位置， 否则有可能出现溢出

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        pre = None
        cur = head
        while cur is not None:
            next_temp = cur.next
            cur.next = pre
            pre = cur
            cur = next_temp
        return pre
