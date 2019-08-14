"""
d地址：https://leetcode-cn.com/problems/sum-of-two-integers/solution/

描述：
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

思路：
a + b 的问题拆分为 (a 和 b 的无进位结果) + (a 和 b 的进位结果)
无进位加法使用异或运算计算得出
进位结果使用与运算和移位运算计算得出
循环此过程，直到进位为 0

在 Python 中的特殊处理
在 Python 中，整数不是 32 位的，也就是说你一直循环左移并不会存在溢出的现象，这就需要我们手动对 Python 中的整数进行处理，手动模拟 32 位 INT 整型。

具体做法是将整数对 0x100000000 取模，保证该数从 32 位开始到最高位都是 0。

"""


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 2^32
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # 计算进位
            carry = (a & b) << 1
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
