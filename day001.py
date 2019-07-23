"""
题目地址：https://leetcode.com/problems/valid-parentheses/description

描述：
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true


思路：
使用栈,遍历输入字符串

如果当前字符为左半边括号时，则将其压入栈中

如果遇到右半边括号时，分类讨论：

1）如栈不为空且为对应的左半边括号，则取出栈顶元素，继续循环

2）若此时栈为空，则直接返回false

3）若不为对应的左半边括号，反之返回false
"""


class Solution:
    @staticmethod
    def isValid(s):
        stack = []
        map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        for x in s:
            if x in map:
                stack.append(map[x])
            else:
                if len(stack) != 0:
                    top_element = stack.pop()
                    if x != top_element:
                        return False
                    else:
                        continue
                else:
                    return False
        return len(stack) == 0


print(Solution.isValid("[]}"))
# print(Solution.isValid("{[]}"))
# print(Solution.isValid("[{]}"))
