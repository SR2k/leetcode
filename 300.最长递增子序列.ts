/*
 * @lc app=leetcode.cn id=300 lang=typescript
 *
 * [300] 最长递增子序列
 *
 * https://leetcode.cn/problems/longest-increasing-subsequence/description/
 *
 * algorithms
 * Medium (53.55%)
 * Likes:    2560
 * Dislikes: 0
 * Total Accepted:    535.6K
 * Total Submissions: 1M
 * Testcase Example:  '[10,9,2,5,3,7,101,18]'
 *
 * 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
 *
 * 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7]
 * 的子序列。
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [10,9,2,5,3,7,101,18]
 * 输出：4
 * 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0,1,0,3,2,3]
 * 输出：4
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [7,7,7,7,7,7,7]
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 2500
 * -10^4 <= nums[i] <= 10^4
 *
 *
 *
 *
 * 进阶：
 *
 *
 * 你能将算法的时间复杂度降低到 O(n log(n)) 吗?
 *
 *
 */

export
// @lc code=start
function lengthOfLIS(nums: number[]): number {
  const top = []

  for (const n of nums) {
    const i = binarySearch(top, n)

    if (i < 0) {
      top.push(n)
    } else {
      top[i] = n
    }
  }

  return top.length
}

const binarySearch = (top: number[], target: number) => {
  if (!top.length) return -1

  let left = 0, right = top.length - 1

  while (left + 1 < right) {
    const middle = Math.floor((left + right) / 2)

    if (top[middle] > target) {
      right = middle
    } else {
      left = middle
    }
  }

  if (top[left] >= target) {
    return left
  }
  if (top[right] >= target) {
    return right
  }
  return -1
}
// @lc code=end
