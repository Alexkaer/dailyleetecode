"""

地址：https://leetcode.com/problems/merge-sorted-array/description/

描述：
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

思路：
这道题目其实和基本排序算法中的merge sort非常像，但是 merge sort 很多时候，合并的时候我们通常是 新建一个数组，这样就很简单。 但是这道题目要求的是原地修改.

这就和 merge sort 的 merge 过程有点不同，我们先来回顾一下 merge sort 的 merge 过程。

merge 的过程可以是先比较两个数组的头元素，然后将较小的推到最终的数组中，并将其从原数组中出队列。 循环直到两个数组都为空。
"""


class Solution:
    @staticmethod
    def merge(nums1, m, nums2, n):
        nums1_copy = nums1[:m]
        nums1[:] = []
        p1 = p2 = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]
        return nums1


print(Solution.merge([1, 3, 5, 7], 4, [2, 4, 6, 8, 10, 12], 6))
print(Solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
