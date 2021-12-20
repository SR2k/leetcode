#
# @lc app=leetcode.cn id=2023 lang=python3
#
# [2023] 连接后等于目标字符串的字符串对
#
# https://leetcode-cn.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/description/
#
# algorithms
# Medium (74.90%)
# Likes:    4
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 4.2K
# Testcase Example:  '["777","7","77","77"]\n"7777"'
#
# 给你一个 数字 字符串数组 nums 和一个 数字 字符串 target ，请你返回 nums[i] + nums[j] （两个字符串连接）结果等于
# target 的下标 (i, j) （需满足 i != j）的数目。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = ["777","7","77","77"], target = "7777"
# 输出：4
# 解释：符合要求的下标对包括：
# - (0, 1)："777" + "7"
# - (1, 0)："7" + "777"
# - (2, 3)："77" + "77"
# - (3, 2)："77" + "77"
# 
# 
# 示例 2：
# 
# 输入：nums = ["123","4","12","34"], target = "1234"
# 输出：2
# 解释：符合要求的下标对包括
# - (0, 1)："123" + "4"
# - (2, 3)："12" + "34"
# 
# 
# 示例 3：
# 
# 输入：nums = ["1","1","1"], target = "11"
# 输出：6
# 解释：符合要求的下标对包括
# - (0, 1)："1" + "1"
# - (1, 0)："1" + "1"
# - (0, 2)："1" + "1"
# - (2, 0)："1" + "1"
# - (1, 2)："1" + "1"
# - (2, 1)："1" + "1"
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= nums.length <= 100
# 1 <= nums[i].length <= 100
# 2 <= target.length <= 100
# nums[i] 和 target 只包含数字。
# nums[i] 和 target 不含有任何前导 0 。
# 
# 
#

# @lc code=start
from collections import Counter


class Solution:
    @staticmethod
    def string_sub(a: str, b: str) -> str:
        if len(a) <= len(b):
            return ''

        if a[:len(b)] != b:
            return ''
        return a[len(b):]

    def numOfPairs(self, nums: list[str], target: str) -> int:
        counter = Counter(nums)
        result = 0

        keys = counter.keys()
        for n in keys:
            sub_result = Solution.string_sub(target, n)
            if not sub_result:
                continue

            if sub_result == n:
                result += counter[n] * (counter[n] - 1)
            else:
                result += counter[sub_result] * counter[n]

        return result
# @lc code=end

s = Solution()
print(s.numOfPairs(nums = ["777","7","77","77"], target = "7777"))
print(s.numOfPairs(nums = ["123","4","12","34"], target = "1234"))
print(s.numOfPairs(nums = ["1","1","1"], target = "11"))
