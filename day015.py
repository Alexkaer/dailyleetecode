"""
地址：https://leetcode.com/problems/number-of-1-bits/description/
描述：
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).



Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.


Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.

思路：
这个题目的大意是： 给定一个无符号的整数， 返回其用二进制表式的时候的1的个数。

这里用一个trick， 可以轻松求出。 就是n & (n - 1) 可以消除 n 最后的一个1的原理。

为什么能消除最后一个1， 其实也比较简单，大家自己想一下

这样我们可以不断进行n = n & (n - 1)直到n === 0 ， 说明没有一个1了。 这个时候我们消除了多少1变成一个1都没有了， 就说明n有多少个1了。
"""


class Solution:
    @staticmethod
    def hammingWeight(n):
        sum = 0
        while n != 0:
            sum += 1
            n &= (n - 1)
        return sum


print(Solution.hammingWeight(7))
print(Solution.hammingWeight(3))
