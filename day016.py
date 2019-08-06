"""
打家劫舍
地址：https://leetcode-cn.com/problems/house-robber/

描述：
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

思路：
这是一道非常典型且简单的动态规划问题，但是在这里我希望通过这个例子， 让大家对动态规划问题有一点认识。

为什么别人的动态规划可以那么写，为什么没有用 dp 数组就搞定了。 比如别人的爬楼梯问题怎么就用 fibnacci 搞定了？为什么？在这里我们就来看下。

思路还是和其他简单的动态规划问题一样，我们本质上在解决对于第[i] 个房子，我们抢还是不抢。的问题。

判断的标准就是总价值哪个更大， 那么对于抢的话就是当前的房子可以抢的价值 + dp[i - 2]

i - 1 不能抢，否则会触发警铃

如果不抢的话，就是dp[i - 1].

这里的 dp 其实就是子问题.

状态转移方程也不难写dp[i] = Math.max(dp[i - 2] + nums[i - 2], dp[i - 1]);.
"""


class Solution:
    @staticmethod
    def rob(nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            pre_max = 0
            cur_max = 0
            for x in nums:
                temp = cur_max
                cur_max = max(pre_max + x, cur_max)
                pre_max = temp
            return cur_max


print(Solution.rob([1, 2, 3, 4, 5, 6]))
