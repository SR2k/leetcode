#
# @lc app=leetcode.cn id=1150 lang=python3
#
# [1150] 检查一个数是否在数组中占绝大多数
#
# https://leetcode-cn.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/description/
#
# algorithms
# Easy (60.53%)
# Likes:    27
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 7.1K
# Testcase Example:  '[2,4,5,5,5,5,5,6,6]\n5'
#
# 给出一个按 非递减 顺序排列的数组 nums，和一个目标数值 target。假如数组 nums 中绝大多数元素的数值都等于 target，则返回
# True，否则请返回 False。
# 
# 所谓占绝大多数，是指在长度为 N 的数组中出现必须 超过 N/2 次。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,4,5,5,5,5,5,6,6], target = 5
# 输出：true
# 解释：
# 数字 5 出现了 5 次，而数组的长度为 9。
# 所以，5 在数组中占绝大多数，因为 5 次 > 9/2。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [10,100,101,101], target = 101
# 输出：false
# 解释：
# 数字 101 出现了 2 次，而数组的长度是 4。
# 所以，101 不是 数组占绝大多数的元素，因为 2 次 = 4/2。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# 
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        # 写二分已经写吐了。。偷个懒
        return Counter(nums)[target] >= len(nums) // 2
# @lc code=end

