/*
 * @lc app=leetcode.cn id=47 lang=typescript
 *
 * [47] 全排列 II
 *
 * https://leetcode.cn/problems/permutations-ii/description/
 *
 * algorithms
 * Medium (64.86%)
 * Likes:    1109
 * Dislikes: 0
 * Total Accepted:    336.8K
 * Total Submissions: 519.3K
 * Testcase Example:  '[1,1,2]'
 *
 * 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,1,2]
 * 输出：
 * [[1,1,2],
 * ⁠[1,2,1],
 * ⁠[2,1,1]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 8
 * -10 <= nums[i] <= 10
 *
 *
 */

export
// @lc code=start
function permuteUnique(nums: number[]): number[][] {
  const result: number[][] = []
  helper(nums, 0, result)
  return result
}

function helper(nums: number[], i: number, result: number[][]) {
  if (i >= nums.length) {
    result.push([...nums])
    return
  }

  const seen = new Set()
  for (let j = i; j < nums.length; j++) {
    if (seen.has(nums[j])) {
      continue
    }
    seen.add(nums[j]);

    [nums[i], nums[j]] = [nums[j], nums[i]]
    helper(nums, i + 1, result);
    [nums[i], nums[j]] = [nums[j], nums[i]]
  }
}
// @lc code=end
