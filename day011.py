"""
地址：https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

描述：
这是leetcode头号题目two sum的第二个版本，难度简单。

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

思路：
由于题目没有对空间复杂度有求，用一个hashmap 存储已经访问过的数字即可。

假如题目空间复杂度有要求，由于数组是有序的，只需要双指针即可。一个left指针，一个right指针， 如果left + right 值 大于target 则 right左移动， 否则left右移，代码比较简单， 不贴了。

如果数组无序，需要先排序（从这里也可以看出排序是多么重要的操作）
"""


class Solution:
    def twoSum(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return left + 1, right + 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return -1, -1


solution = Solution()
print(solution.twoSum([2, 7, 11, 15, 20], 13))
