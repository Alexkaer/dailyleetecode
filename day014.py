"""
地址：https://leetcode-cn.com/problems/reverse-bits/

描述：
Reverse bits of a given 32 bits unsigned integer.



Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10101111110010110010011101101001.


Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.

思路：
这道题是给定一个32位的无符号整型，让你按位翻转， 第一位变成最后一位， 第二位变成倒数第二位。。。

那么思路就是双指针

这个指针可以加引号

n从高位开始逐步左， res从低位（0）开始逐步右移
逐步判断，如果该位是1，就res + 1 , 如果是该位是0， 就res + 0
32位全部遍历完，则遍历结束

关键点分析：
可以用任何数字和1进行位运算的结果都取决于该数字最后一位的特性简化操作和提高性能
eg :

n & 1 === 1, 说明n的最后一位是1
n & 1 === 0, 说明n的最后一位是0
对于JS，ES规范在之前很多版本都是没有无符号整形的， 转化为无符号，可以用一个trickn >>> 0

双"指针" 模型

bit 运算



Python 一行代码：

n 转为二进制并去掉前缀 0b
左侧填充 0 到 32 位
翻转字符串
转为十进制表示
"""


class Solution:
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], base=2)
