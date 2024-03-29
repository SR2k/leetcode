#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#
# https://leetcode.cn/problems/shuffle-an-array/description/
#
# algorithms
# Medium (61.13%)
# Likes:    283
# Dislikes: 0
# Total Accepted:    101.7K
# Total Submissions: 166.3K
# Testcase Example:  '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
#
# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该是 等可能 的。
# 
# 实现 Solution class:
# 
# 
# Solution(int[] nums) 使用整数数组 nums 初始化对象
# int[] reset() 重设数组到它的初始状态并返回
# int[] shuffle() 返回数组随机打乱后的结果
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# 输出
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
# 
# 解释
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3,
# 1, 2]
# solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
# solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 50
# -10^6 <= nums[i] <= 10^6
# nums 中的所有元素都是 唯一的
# 最多可以调用 10^4 次 reset 和 shuffle
# 
# 
#

# @lc code=start
from random import randrange


class Solution:
    def __init__(self, nums: list[int]):
        self.nums = nums


    def reset(self) -> list[int]:
        return self.nums


    def shuffle(self) -> list[int]:
        result = [x for x in self.nums]

        for i in range(len(self.nums) - 1, 0, -1):
            rand = randrange(0, i + 1)
            result[i], result[rand] = result[rand], result[i]

        return result
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

