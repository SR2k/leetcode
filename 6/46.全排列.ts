/*
 * @lc app=leetcode.cn id=46 lang=typescript
 *
 * [46] 全排列
 *
 * https://leetcode.cn/problems/permutations/description/
 *
 * algorithms
 * Medium (78.61%)
 * Likes:    2088
 * Dislikes: 0
 * Total Accepted:    650.1K
 * Total Submissions: 826.9K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0,1]
 * 输出：[[0,1],[1,0]]
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1]
 * 输出：[[1]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 6
 * -10 <= nums[i] <= 10
 * nums 中的所有整数 互不相同
 *
 *
 */

export
// @lc code=start
function permute(nums: number[]): number[][] {
  const result: number[][] = []
  helper(nums, 0, result)
  return result
}

function helper(nums: number[], i: number, result: number[][]) {
  if (i >= nums.length) {
    result.push([...nums])
    return
  }

  for (let j = i; j < nums.length; j++) {
    [nums[i], nums[j]] = [nums[j], nums[i]]
    helper(nums, i + 1, result);
    [nums[i], nums[j]] = [nums[j], nums[i]]
  }
}
// @lc code=end
