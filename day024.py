"""
地址：https://leetcode.com/problems/power-of-four/description/  不实用循环递归完成

描述：
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

思路：
这道题是在leetcodeNo.231:2的幂的基础上的扩展，因此解法也只需要在该题的解法上扩展即可。

首先可以发现，4的幂是2的幂的子集，所以首先判断是否是2的幂。(n & (n - 1) 一定等于 0)

关于如何判断是否是2的幂，可以参见我在#231发布的题解。

其次，观察4的幂的二进制表示可以发现，其长度总为奇数，也就是说，1的位置总是在奇数位上。

因此如果有一个数的二进制表示只有奇数位上为1，那么这个数和4的幂做与运算，得到的还是4的幂本身。

题目要求的是32位整数，因此这个数就是0b1010101010101010101010101010101，这么长看起来很不优雅，

所以我们可以将它转化为16进制表示0x55555555，这样看起来就好多了

"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and (num & num - 1) == 0 and (num & 0x55555555) == num
