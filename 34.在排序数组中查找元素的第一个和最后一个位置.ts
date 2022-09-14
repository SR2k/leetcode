/*
 * @lc app=leetcode.cn id=34 lang=typescript
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 *
 * https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
 *
 * algorithms
 * Medium (42.31%)
 * Likes:    1892
 * Dislikes: 0
 * Total Accepted:    641K
 * Total Submissions: 1.5M
 * Testcase Example:  '[5,7,7,8,8,10]\n8'
 *
 * 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
 *
 * 如果数组中不存在目标值 target，返回 [-1, -1]。
 *
 * 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [5,7,7,8,8,10], target = 8
 * 输出：[3,4]
 *
 * 示例 2：
 *
 *
 * 输入：nums = [5,7,7,8,8,10], target = 6
 * 输出：[-1,-1]
 *
 * 示例 3：
 *
 *
 * 输入：nums = [], target = 0
 * 输出：[-1,-1]
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * nums 是一个非递减数组
 * -10^9 <= target <= 10^9
 *
 *
 */

export
// @lc code=start
function searchRange(nums: number[], target: number): number[] {
  const first = biSearch(nums, target, SearchModes.First)
  if (first < 0) return [-1, -1]

  return [
    first,
    biSearch(nums, target, SearchModes.Last, first),
  ]
}

function biSearch(nums: number[], target: number, mode: SearchModes, left = 0, right = nums.length - 1) {
  if (!nums.length) return -1

  while (left + 1 < right) {
    const middle = (left + right) >> 1

    if (nums[middle] > target) {
      right = middle
    } else if (nums[middle] < target) {
      left = middle
    } else if (mode === SearchModes.First) {
      right = middle
    } else {
      left = middle
    }
  }

  const equals = [left, right].filter((x) => nums[x] === target)
  if (!equals.length) return -1

  if (mode === SearchModes.First) return Math.min(...equals)
  return Math.max(...equals)
}

const enum SearchModes {
  First,
  Last,
}
// @lc code=end
