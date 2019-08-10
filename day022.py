"""
丑陋数
地址：https://leetcode.com/problems/ugly-number/description/
描述：
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].
思路：
题目要求给定一个数字，判断是否为“丑陋数”(ugly number), 丑陋数是指只包含质因子2, 3, 5的正整数。
根据定义，我们将给定数字除以2、3、5(顺序无所谓)，直到无法整除。 如果得到1，说明是所有因子都是2或3或5，如果不是1，则不是丑陋数。

这就好像我们判断一个数字是否为n(n为大于1的正整数)的幂次方一样，我们只需要 不断除以n，直到无法整除，如果得到1，那么就是n的幂次方。 这道题的不同在于 它不再是某一个数字的幂次方，而是三个数字（2，3，5），不过解题思路还是一样的。
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        return num == 1


so = Solution()
print(so.isUgly(6))
print(so.isUgly(7))
