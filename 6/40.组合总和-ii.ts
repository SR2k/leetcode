/*
 * @lc app=leetcode.cn id=40 lang=typescript
 *
 * [40] 组合总和 II
 *
 * https://leetcode.cn/problems/combination-sum-ii/description/
 *
 * algorithms
 * Medium (60.65%)
 * Likes:    1017
 * Dislikes: 0
 * Total Accepted:    312.1K
 * Total Submissions: 514.6K
 * Testcase Example:  '[10,1,2,7,6,1,5]\n8'
 *
 * 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
 *
 * candidates 中的每个数字在每个组合中只能使用 一次 。
 *
 * 注意：解集不能包含重复的组合。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: candidates = [10,1,2,7,6,1,5], target = 8,
 * 输出:
 * [
 * [1,1,6],
 * [1,2,5],
 * [1,7],
 * [2,6]
 * ]
 *
 * 示例 2:
 *
 *
 * 输入: candidates = [2,5,2,1,2], target = 5,
 * 输出:
 * [
 * [1,2,2],
 * [5]
 * ]
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= candidates.length <= 100
 * 1 <= candidates[i] <= 50
 * 1 <= target <= 30
 *
 *
 */

export
// @lc code=start
function combinationSum2(candidates: number[], target: number): number[][] {
  candidates.sort((a, b) => a - b)

  function helper(i = 0, curr: number[] = [], sum = 0, result: number[][] = []) {
    if (i >= candidates.length) {
      if (sum === target) {
        result.push(curr.concat([]))
      }
      return result
    }

    helper(i + 1, curr, sum, result)

    if (i > 0 && candidates[i] === candidates[i - 1]) {
      return result
    }

    const candidate = candidates[i]
    let j = i
    let count = 0

    while (true) {
      if (j >= candidates.length) break
      if (candidates[j] !== candidate) break
      if (sum + candidate > target) break

      sum += candidate
      curr.push(candidate)
      count++
      helper(i + 1, curr, sum, result)

      j++
    }

    for (let x = 0; x < count; x++) {
      curr.pop()
    }

    return result
  }

  return helper()
}
// @lc code=end
