/*
 * @lc app=leetcode.cn id=78 lang=typescript
 *
 * [78] 子集
 *
 * https://leetcode-cn.com/problems/subsets/description/
 *
 * algorithms
 * Medium (80.35%)
 * Likes:    1483
 * Dislikes: 0
 * Total Accepted:    372.7K
 * Total Submissions: 463.9K
 * Testcase Example:  '[1,2,3]'
 *
 * 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
 *
 * 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
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
 * nums 中的所有元素 互不相同
 *
 *
 */

export
// @lc code=start
function subsets(nums: number[]): number[][] {
  const result: number[][] = []

  function helper(prev: number[], i: number) {
    if (i >= nums.length) {
      result.push([...prev])
      return
    }

    helper(prev, i + 1)

    prev.push(nums[i])
    helper(prev, i + 1)
    prev.pop()
  }
  helper([], 0)

  return result
}
// @lc code=end
