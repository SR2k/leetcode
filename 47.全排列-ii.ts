/*
 * @lc app=leetcode.cn id=47 lang=typescript
 *
 * [47] 全排列 II
 *
 * https://leetcode.cn/problems/permutations-ii/description/
 *
 * algorithms
 * Medium (65.08%)
 * Likes:    1162
 * Dislikes: 0
 * Total Accepted:    363.7K
 * Total Submissions: 558.7K
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

  function helper(i: number) {
    if (i >= nums.length) {
      result.push([...nums])
      return
    }

    helper(i + 1)

    const seen = new Set<number>([nums[i]])

    for (let j = i + 1; j < nums.length; j++) {
      if (seen.has(nums[j])) continue
      seen.add(nums[j])

      swap(nums, i, j)
      helper(i + 1)
      swap(nums, i, j)
    }
  }

  helper(0)
  return result
}

function swap(arr: any[], i: number, j: number) {
  const temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}
// @lc code=end
