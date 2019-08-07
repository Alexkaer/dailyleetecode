"""
地址：https://leetcode.com/problems/remove-linked-list-elements/description/

描述：
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5


思路：
这个一个链表基本操作的题目，思路就不多说了。

关键点：
链表的基本操作（删除指定节点）
虚拟节点dummy 简化操作
其实设置dummy节点就是为了处理特殊位置（头节点），这这道题就是如果头节点是给定的需要删除的节点呢？ 为了保证代码逻辑的一致性，即不需要为头节点特殊定制逻辑，才采用的虚拟节点。

如果连续两个节点都是要删除的节点，这个情况容易被忽略。 eg:
// 只有下个节点不是要删除的节点才更新current
if (!next || next.val !== val) {
    current =  next;
}
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = next


class Solution(object):
    @staticmethod
    def removeElements(head, val):
        dummy_node = ListNode(val - 1)
        dummy_node.next = head
        prev = dummy_node
        while prev.next is not None:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy_node.next
