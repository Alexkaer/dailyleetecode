"""
地址：https://leetcode.com/problems/path-sum-iii/description/
描述：
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 时间复杂度还挺好，超过90%+
def pathSum(self, root, sum):
    if not root:
        return 0

    # sums为node的父节点已能构成的和，返回到node结束的所有路径所能构成的和列表
    def dfs(node, sums):
        left = right = 0  # 左右的值默认为0
        # 之前的和加当前结点值能构成的新和，以及从当前结点开始算的新和
        temp = [num + node.val for num in sums] + [node.val]
        if node.left:
            left = dfs(node.left, temp)  # 递归
        if node.right:
            right = dfs(node.right, temp)  # 递归
        return temp.count(sum) + left + right

    return dfs(root, [])
