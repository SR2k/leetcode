/*
 * @lc app=leetcode.cn id=40 lang=typescript
 *
 * [40] 组合总和 II
 *
 * https://leetcode-cn.com/problems/combination-sum-ii/description/
 *
 * algorithms
 * Medium (61.73%)
 * Likes:    752
 * Dislikes: 0
 * Total Accepted:    218.2K
 * Total Submissions: 353.5K
 * Testcase Example:  '[10,1,2,7,6,1,5]\n8'
 *
 * 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
 *
 * candidates 中的每个数字在每个组合中只能使用一次。
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
 * 1
 * 1
 * 1
 *
 *
 */

export
// @lc code=start
function combinationSum2(candidates: number[], target: number): number[][] {
  const counter: Map<number, number> = new Map()
  for (const c of candidates) {
    counter.set(c, 1 + (counter.get(c) || 0))
  }
  // const c = Object.fromEntries(counter.entries())
  const keys = [...counter.keys()]

  const result: number[][] = []

  function helper(prev: number[], prevSum: number, i: number) {
    if (i >= keys.length) {
      if (prevSum === target) {
        result.push([...prev])
      }
      return
    }
    if (prevSum > target) return

    const candidate = keys[i]
    const count = counter.get(candidate)!

    for (let m = 0; m < count; m++) {
      prev.push(candidate)
      prevSum += candidate
      helper(prev, prevSum, i + 1)
    }

    for (let m = 0; m < count; m++) {
      prevSum -= candidate
      prev.pop()
    }
    helper(prev, prevSum, i + 1)
  }
  helper([], 0, 0)

  return result
}
// @lc code=end
