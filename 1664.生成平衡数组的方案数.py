#
# @lc app=leetcode.cn id=1664 lang=python3
#
# [1664] 生成平衡数组的方案数
#
# https://leetcode-cn.com/problems/ways-to-make-a-fair-array/description/
#
# algorithms
# Medium (54.92%)
# Likes:    28
# Dislikes: 0
# Total Accepted:    5.6K
# Total Submissions: 10.3K
# Testcase Example:  '[2,1,6,4]'
#
# 给你一个整数数组 nums 。你需要选择 恰好 一个下标（下标从 0 开始）并删除对应的元素。请注意剩下元素的下标可能会因为删除操作而发生改变。
# 
# 比方说，如果 nums = [6,1,7,4,1] ，那么：
# 
# 
# 选择删除下标 1 ，剩下的数组为 nums = [6,7,4,1] 。
# 选择删除下标 2 ，剩下的数组为 nums = [6,1,4,1] 。
# 选择删除下标 4 ，剩下的数组为 nums = [6,1,7,4] 。
# 
# 
# 如果一个数组满足奇数下标元素的和与偶数下标元素的和相等，该数组就是一个 平衡数组 。
# 
# 请你返回删除操作后，剩下的数组 nums 是 平衡数组 的 方案数 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,1,6,4]
# 输出：1
# 解释：
# 删除下标 0 ：[1,6,4] -> 偶数元素下标为：1 + 4 = 5 。奇数元素下标为：6 。不平衡。
# 删除下标 1 ：[2,6,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：6 。平衡。
# 删除下标 2 ：[2,1,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：1 。不平衡。
# 删除下标 3 ：[2,1,6] -> 偶数元素下标为：2 + 6 = 8 。奇数元素下标为：1 。不平衡。
# 只有一种让剩余数组成为平衡数组的方案。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,1,1]
# 输出：3
# 解释：你可以删除任意元素，剩余数组都是平衡数组。
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1,2,3]
# 输出：0
# 解释：不管删除哪个元素，剩下数组都不是平衡数组。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        prefix_sum = [[0, 0]]

        for i, n in enumerate(nums):
            prev = prefix_sum[-1]
            if i % 2:
                prefix_sum.append([prev[0] + n, prev[1]])
            else:
                prefix_sum.append([prev[0], prev[1] + n])

        result = 0
        for i, n in enumerate(nums):
            left = prefix_sum[i]
            right = [
                prefix_sum[-1][1] - prefix_sum[i + 1][1],
                prefix_sum[-1][0] - prefix_sum[i + 1][0], 
            ]
            if left[0] + right[0] == left[1] + right[1]:
                result += 1

        return result
# @lc code=end

s = Solution()
print(s.waysToMakeFair(nums = [2,1,6,4]))
print(s.waysToMakeFair(nums = [1,1,1]))
print(s.waysToMakeFair(nums = [1,2,3]))
