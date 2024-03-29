"""
题目地址：https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

题目描述：
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length. Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length. Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.


思路：
使用快慢指针来记录遍历的坐标。

开始时这两个指针都指向第一个数字

如果两个指针指的数字相同，则快指针向前走一步

如果不同，则两个指针都向前走一步

当快指针走完整个数组后，慢指针当前的坐标加1就是数组中不同数字的个数

解析：
双指针
这道题如果不要求，O(n)的时间复杂度， O(1)的空间复杂度的话，会很简单。 但是这道题是要求的，这种题的思路一般都是采用双指针

如果是数据是无序的，就不可以用这种方式了，从这里也可以看出排序在算法中的基础性和重要性。


"""


class Solution:
    @staticmethod
    def removeDuplicates(nums):
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        slowP = 0
        fastP = 1
        while fastP < len(nums):
            if nums[slowP] != nums[fastP]:
                slowP += 1
                nums[slowP] = nums[fastP]
                fastP += 1
            else:
                fastP += 1

        return slowP+1


print(Solution.removeDuplicates([2,2,2,2,2]))
print(Solution.removeDuplicates([1,2,2,2,2]))
print(Solution.removeDuplicates([1,1,1,1,2]))
