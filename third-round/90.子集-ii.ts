/*
 * @lc app=leetcode.cn id=90 lang=typescript
 *
 * [90] 子集 II
 *
 * https://leetcode-cn.com/problems/subsets-ii/description/
 *
 * algorithms
 * Medium (63.39%)
 * Likes:    737
 * Dislikes: 0
 * Total Accepted:    165.9K
 * Total Submissions: 261.8K
 * Testcase Example:  '[1,2,2]'
 *
 * 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
 *
 * 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,2]
 * 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0]
 * 输出：[[],[0]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * -10
 *
 *
 *
 *
 */

export
// @lc code=start
function subsetsWithDup(nums: number[]): number[][] {
  const counter = new Map<number, number>()
  for (const n of nums) {
    counter.set(n, (counter.get(n) || 0) + 1)
  }
  const options = [...counter.keys()]

  const result: number[][] = []
  function helper(prev: number[], i: number) {
    if (i >= options.length) {
      result.push([...prev])
      return
    }

    helper(prev, i + 1)

    const option = options[i]
    const count = counter.get(option)!
    for (let n = 0; n < count; n++) {
      prev.push(option)
      helper(prev, i + 1)
    }
    for (let n = 0; n < count; n++) {
      prev.pop()
    }
  }
  helper([], 0)

  return result
}
// @lc code=end
