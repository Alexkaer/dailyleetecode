"""
地址：https://leetcode-cn.com/problems/majority-element/

描述：
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

思路：
符合直觉的做法是利用额外的空间去记录每个元素出现的次数，并用一个单独的变量记录当前出现次数最多的元素。

但是这种做法空间复杂度较高，有没有可能进行优化呢？ 答案就是用"投票算法"。

投票算法的原理是通过不断消除不同元素直到没有不同元素，剩下的元素就是我们要找的元素。
"""


class Solution:
    @staticmethod
    def majorityElement(nums):
        count = candiate = 0
        for i in nums:
            if count == 0:
                candiate = i
            count += (1 if candiate == i else -1)
        return candiate


print(Solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
