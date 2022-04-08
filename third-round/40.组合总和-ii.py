#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (61.25%)
# Likes:    865
# Dislikes: 0
# Total Accepted:    252.1K
# Total Submissions: 412.3K
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
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        counter = Counter(candidates)
        candidates = list(counter.keys())

        curr = []
        result = []

        def helper(i: int, prev_sum: int):
            if i >= len(candidates):
                if prev_sum == target:
                    result.append([] + curr)
                return

            if prev_sum > target:
                return

            helper(i + 1, prev_sum)

            candidate = candidates[i]
            cnt = counter[candidate]
            for _ in range(cnt):
                curr.append(candidate)
                prev_sum += candidate
                helper(i + 1, prev_sum)

            for _ in range(cnt):
                curr.pop()

        helper(0, 0)
        return result
# @lc code=end

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], target = 8))
print(s.combinationSum2([2,5,2,1,2], target = 5))
