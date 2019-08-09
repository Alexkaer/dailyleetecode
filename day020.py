"""
地址：https://leetcode.com/problems/invert-binary-tree/description/

描述：
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

思路：
遍历树（随便怎么遍历），然后将左右子树交换位置

关键点：
递归简化操作
如果树很高，建议使用栈来代替递归
这道题目对顺序没要求的，因此队列数组操作都是一样的，无任何区别

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        left = root.left
        right = root.right
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)
        return root
