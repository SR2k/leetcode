#
# @lc app=leetcode.cn id=945 lang=python3
#
# [945] 使数组唯一的最小增量
#
# https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/description/
#
# algorithms
# Medium (48.71%)
# Likes:    177
# Dislikes: 0
# Total Accepted:    34.5K
# Total Submissions: 70.9K
# Testcase Example:  '[1,2,2]'
#
# 给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
# 
# 返回使 A 中的每个值都是唯一的最少操作次数。
# 
# 示例 1:
# 
# 输入：[1,2,2]
# 输出：1
# 解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
# 
# 示例 2:
# 
# 输入：[3,2,1,2,1,7]
# 输出：6
# 解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
# 可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
# 
# 
# 提示：
# 
# 
# 0 <= A.length <= 40000
# 0 <= A[i] < 40000
# 
# 
#

# @lc code=start
# from sortedcontainers import SortedSet


# def b_find(ss: SortedSet[int], n: int) -> int:
#     left, right = 0, len(ss) - 1

#     while left + 1 < right:
#         middle = (left + right) // 2

#         if ss[middle] > n:
#             right = middle
#         else:
#             left = middle

#     if ss[left] > n:
#         return ss[left]
#     if ss[right] > n:
#         return ss[right]
#     return ss[right] + 1


# class Solution:
#     def minIncrementForUnique(self, nums: list[int]) -> int:
#         if not nums:
#             return 0

#         min_n, max_n = min(nums), max(nums) + len(nums)
#         avaliable = SortedSet(range(min_n, max_n + 1))
#         ret = 0

#         for n in nums:
#             if n in avaliable:
#                 avaliable.remove(n)
#             else:
#                 a  = b_find(avaliable, n)
#                 ret += a - n
#                 avaliable.remove(a)

#         return ret


class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        ret = 0
        for i, n in enumerate(nums):
            if i == 0:
                continue
            if n <= nums[i - 1]:
                ret += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1

        return ret
# @lc code=end
