#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (72.74%)
# Likes:    1715
# Dislikes: 0
# Total Accepted:    394.9K
# Total Submissions: 542.8K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target
# 的 所有不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
# 
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
# 
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。
# 
# 示例 2：
# 
# 
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]
# 
# 示例 3：
# 
# 
# 输入: candidates = [2], target = 1
# 输出: []
# 
# 
# 示例 4：
# 
# 
# 输入: candidates = [1], target = 1
# 输出: [[1]]
# 
# 
# 示例 5：
# 
# 
# 输入: candidates = [1], target = 2
# 输出: [[1,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都 互不相同
# 1 <= target <= 500
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def helper(curr: list[int], curr_sum: int, i: int):
            if i >= len(candidates):
                if curr_sum == target:
                    result.append([n for n in curr])
                return

            added_cnt = 0
            while candidates[i] + curr_sum <= target:
                curr.append(candidates[i])
                curr_sum += candidates[i]
                helper(curr, curr_sum, i + 1)
                added_cnt += 1

            for _ in range(added_cnt):
                curr_sum -= candidates[i]
                curr.pop()

            helper(curr, curr_sum, i + 1)

        helper([], 0, 0)
        return result
# @lc code=end

s = Solution()
print(s.combinationSum(candidates = [2,3,6,7], target = 7))
print(s.combinationSum(candidates = [2,3,5], target = 8))
print(s.combinationSum(candidates = [2], target = 1))
print(s.combinationSum(candidates = [1], target = 1))
print(s.combinationSum(candidates = [1], target = 2))
