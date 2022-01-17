#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (61.73%)
# Likes:    752
# Dislikes: 0
# Total Accepted:    218.2K
# Total Submissions: 353.5K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
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
# 1 
# 1 
# 1 
# 
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        c = Counter(candidates)
        nums = list(c.keys())
        len_nums = len(nums)

        candidates.sort()

        def helper(prev_list: list[int], prev_index: int, prev_sum: int):
            if prev_sum == target:
                result.append(prev_list + [])
                return
            if prev_sum >= target or prev_index == len_nums - 1:
                return

            next_num = nums[prev_index + 1]
            iteration_count = 0

            for _ in range(c[next_num]):
                iteration_count += 1
                prev_list.append(next_num)
                prev_sum += next_num
                if prev_sum > target:
                    break
                helper(prev_list, prev_index + 1, prev_sum)

            for _ in range(iteration_count):
                prev_sum -= next_num
                prev_list.pop()
            helper(prev_list, prev_index + 1, prev_sum)

        helper([], -1, 0)
        return result
# @lc code=end

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
print(s.combinationSum2([2,5,2,1,2], 5))
