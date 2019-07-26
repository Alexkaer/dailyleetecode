"""
地址：https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

描述：
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

思路：
由于树是一种递归的数据结构，因此用递归去解决的时候往往非常容易.
如果使用迭代呢？ 我们首先应该想到的是树的各种遍历，由于我们求的是深度，因此 使用层次遍历（BFS）是非常合适的。 我们只需要记录有多少层即可。相关思路请查看binary-tree-traversal

关键点：
队列

队列中用 Null(一个特殊元素)来划分每层，或者在对每层进行迭代之前保存当前队列元素的个数（即当前层所含元素个数）

树的基本操作- 遍历 - 层次遍历（BFS）


"""


class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


solution = Solution()
rootTree = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
print(solution.maxDepth(rootTree))
