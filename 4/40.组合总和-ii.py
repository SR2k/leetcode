#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (60.91%)
# Likes:    910
# Dislikes: 0
# Total Accepted:    270.8K
# Total Submissions: 444.6K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用 一次 。
# 
# 注意：解集不能包含重复的组合。 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 
# 示例 2:
# 
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
# 
# 
# 
# 提示:
# 
# 
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# 
# 
#

# @lc code=start
# from collections import Counter


# class Solution:
#     def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
#         counter = Counter(candidates)
#         nums = list(counter.keys())
#         result = []


#         def helper(i: int, prev_sum: int, prev: list[int]):
#             if prev_sum == target:
#                 result.append(prev + [])
#                 return
#             if i >= len(nums) or prev_sum > target:
#                 return

#             helper(i + 1, prev_sum, prev)

#             n = nums[i]
#             for _ in range(counter[n]):
#                 prev_sum += n
#                 prev.append(n)
#                 helper(i + 1, prev_sum, prev)

#             for _ in range(counter[n]):
#                 prev.pop()


#         helper(0, 0, [])
#         return result

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def helper(i: int, sum: int, combination: list[int]):
            if i == len(candidates):
                if sum == target:
                    result.append([] + combination)
                return
            if sum > target:
                return

            helper(i + 1, sum, combination)

            if i > 0 and candidates[i] == candidates[i - 1]:
                return

            c = candidates[i]
            cnt = 0
            while i < len(candidates) and candidates[i] == c:
                combination.append(c)
                sum += c
                helper(i + 1, sum, combination)
                i += 1
                cnt += 1

            for _ in range(cnt):
                combination.pop()


        helper(0, 0, [])
        return result
# @lc code=end
