"""
地址：https://leetcode.com/problems/contains-duplicate-ii/description/
描述：
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

思路：
由于题目没有对空间复杂度有求，用一个hashmap 存储已经访问过的数字即可, 每次访问都会看hashmap中是否有这个元素，有的话拿出索引进行比对，是否满足条件（相隔不大于k），如果满足返回true即可。
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        size = len(nums)
        if size == 0:
            return False
        map = dict()
        for i in range(size):
            if nums[i] in map and i - map[nums[i]] <= k:
                return True
            else:
                map[nums[i]] = i
        return False
