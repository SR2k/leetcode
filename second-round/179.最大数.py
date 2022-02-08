#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# https://leetcode-cn.com/problems/largest-number/description/
#
# algorithms
# Medium (41.01%)
# Likes:    864
# Dislikes: 0
# Total Accepted:    133.8K
# Total Submissions: 326.1K
# Testcase Example:  '[10,2]'
#
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
# 
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [10,2]
# 输出："210"
# 
# 示例 2：
# 
# 
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1]
# 输出："1"
# 
# 
# 示例 4：
# 
# 
# 输入：nums = [10]
# 输出："10"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [str(n) for n in nums]
        def cmp(a: str, b: str) -> str:
            i = 0
            res1, res2 = a + b, b + a

            for i in range(len(res1)):
                if res1[i] != res2[i]:
                    return ord(res2[i]) - ord(res1[i])

            return 0

        nums.sort(key=cmp_to_key(cmp))
        if nums[0] == '0':
            return '0'

        return "".join(nums)
# @lc code=end
