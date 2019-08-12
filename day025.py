"""
地址：https://leetcode-cn.com/problems/intersection-of-two-arrays/ 两数组交集

描述：Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

思路：
方法一：两个 set
幼稚的方法是根据第一个数组 nums1 迭代并检查每个值是否存在在 nums2 内。如果存在将值添加到输出。这样的方法会导致 O(n \times m)O(n×m) 的时间复杂性，其中 n 和 m 是数组的长度。

为了在线性时间内解决这个问题，我们使用集合 set，在 O(1)O(1) 时间复杂度实现操作。

其思想是将两个数组转换为集合 set，然后迭代较小的集合检查是否存在在较大集合中。平均情况下，这种方法的时间复杂度为 O(n+m)O(n+m)。

"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return [x for x in set1 if x in set2]


"""
方法二：内置函数
内置的函数在一般情况下的时间复杂度是 O(n+m)O(n+m) 且时间复杂度最坏的情况是 O(n \times m)O(n×m) 。

在 Python 中提供了交集的操作，在 Java 提供了 retainAll() 函数.

"""


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)
