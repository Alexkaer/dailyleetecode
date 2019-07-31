"""
地址：
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

描述：
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

思路：
这是一道非常适合训练递归的题目。虽然题目不难，但是要想一次写正确，并且代码要足够优雅却不是很容易。

这里我们的思路是定一个递归的helper函数，用来帮助我们完成递归操作。 递归函数的功能是将它的左右子树相加，注意这里不包括这个节点本身，否则会多加， 我们其实关注的就是叶子节点的值，然后通过层层回溯到root，返回即可。


"""


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumNum(self, root, sumall):
        if root is None:
            return 0
        sumall = sumall * 10 + root.val
        if root.left is None and root.right is None:
            return sumall
        return self.sumNum(root.left, sumall) + self.sumNum(root.right, sumall)

    def sumNumbers(self, root):
        if root is None:
            return 0
        return self.sumNum(root, 0)


solution = Solution()
rootTree = TreeNode(3, TreeNode(9, None, None), TreeNode(2, TreeNode(1, None, None), TreeNode(7, None, None)))
print(solution.sumNumbers(rootTree))
