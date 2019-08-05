"""
地址：
https://leetcode.com/problems/factorial-trailing-zeroes/description/


描述：
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.

思路：
我们需要求解这n个数字相乘的结果末尾有多少个0，由于题目要求log的复杂度，因此暴力求解是不行的。

通过观察，我们发现如果想要结果末尾是0，必须是分解质因数之后，2 和 5 相乘才行，同时因数分解之后发现5的个数远小于2， 因此我们只需要求解这n数字分解质因数之后一共有多少个5即可.


"""


class Solution:
    def trailingZeroes(self, num):
        if num < 5:
            return 0
        else:
            return int(num / 5) + self.trailingZeroes(num / 5)


solution = Solution()
print(solution.trailingZeroes(31))
print(solution.trailingZeroes(6))
