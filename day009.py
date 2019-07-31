"""
地址：https://leetcode.com/problems/single-number/description/

描述：
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

思路：
根据题目描述，由于加上了时间复杂度必须是 O(n)，并且空间复杂度为 O(1)的条件，因此不能用排序方法，也不能使用 map 数据结构。

我们可以利用二进制异或的性质来完成，将所有数字异或即得到唯一出现的数字。

关键点：
异或的性质 两个数字异或的结果a^b是将 a 和 b 的二进制每一位进行运算，得出的数字。 运算的逻辑是 如果同一位的数字相同则为 0，不同则为 1

异或的规律

任何数和本身异或则为0

任何数和 0 异或是本身

很多人只是记得异或的性质和规律，但是缺乏对其本质的理解，导致很难想到这种解法（我本人也没想到）

bit 运算
"""


class Solution:
    @staticmethod
    def singleNumber(nums):
        a = 0
        for i in nums:
            a ^= i
        return a


print(Solution.singleNumber([1, 1, 2, 2, 3, 4, 4, 5, 5]))
