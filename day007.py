"""
地址：https://leetcode.com/problems/valid-palindrome/description/

描述：
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

思路：
这是一道考察回文的题目，而且是最简单的形式，即判断一个字符串是否是回文。

针对这个问题，我们可以使用头尾双指针，

如果两个指针的元素不相同，则直接返回false,
如果两个指针的元素相同，我们同时更新头尾指针，循环。 直到头尾指针相遇。
时间复杂度为O(n).

方法二
回文反转后，和原来还是一样
"""


class Solution:
    @staticmethod
    def isPalindrome(s):
        s1 = filter(str.isalnum, s)
        s2 = "".join(s1)
        s3 = s2.lower()
        s_reverse = s3[::-1]
        if s_reverse == s3:
            return True
        else:
            return False


print(Solution.isPalindrome("A man, a plan, a canal: Panama"))
print(Solution.isPalindrome("race a car"))
