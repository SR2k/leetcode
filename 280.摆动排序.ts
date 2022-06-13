/*
 * @lc app=leetcode.cn id=280 lang=typescript
 *
 * [280] 摆动排序
 *
 * https://leetcode.cn/problems/wiggle-sort/description/
 *
 * algorithms
 * Medium (68.73%)
 * Likes:    94
 * Dislikes: 0
 * Total Accepted:    7.5K
 * Total Submissions: 10.9K
 * Testcase Example:  '[3,5,2,1,6,4]'
 *
 * 给你一个的整数数组 nums, 将该数组重新排序后使 nums[0] <= nums[1] >= nums[2] <= nums[3]...
 *
 * 输入数组总是有一个有效的答案。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入：nums = [3,5,2,1,6,4]
 * 输出：[3,5,1,6,2,4]
 * 解释：[1,6,2,5,3,4]也是有效的答案
 *
 * 示例 2:
 *
 *
 * 输入：nums = [6,6,5,6,3,8]
 * 输出：[6,6,5,6,3,8]
 *
 *
 *
 *
 * 提示：
 *
 *
 *
 *
 * 1 <= nums.length <= 5 * 10^4
 * 0 <= nums[i] <= 10^4
 *
 * 输入的 nums 保证至少有一个答案。
 *
 *
 *
 *
 *
 * 进阶：你能在 O(n) 时间复杂度下解决这个问题吗？
 *
 */

export
// @lc code=start
/**
 Do not return anything, modify nums in-place instead.
 */
function wiggleSort(nums: number[]): void {
  quickSelect(nums, Math.ceil(nums.length / 2), 0, nums.length - 1, (a, b) => a - b, mapWiggleInex)
}

interface MapIndex<T> {
  (i: number, arr: T[]): number
}

interface Compare<T> {
  (a: T, b: T): number
}

// 0 1 2 3 4 5 6 7
// 0 2 4 6 1 3 5 7

// 0 1 2 3 4 5 6
// 0 2 4 6 1 3 5

function mapWiggleInex(i: number, nums: any[]) {
  const len = nums.length

  if (i < len / 2) {
    return i * 2
  }

  return i * 2 - ((len - 1) * 2 - (len - (len % 2) - 1))
}

function quickSelect<T>(arr: T[], k: number, left: number, right: number, cmp: Compare<T>, mapIndex: MapIndex<T>) {
  if (left >= right) return

  const i = partition(arr, left, right, cmp, mapIndex)
  const target = right - k + 1

  if (i > target) {
    quickSelect(arr, i - target, left, i - 1, cmp, mapIndex)
  } else if (i < target) {
    quickSelect(arr, k, i + 1, right, cmp, mapIndex)
  }
}

function partition<T>(arr: T[], left: number, right: number, cmp: Compare<T>, mapIndex: MapIndex<T>) {
  const pivot = arr[mapIndex(left, arr)]
  let i = left, j = right
  while (i < j) {
    while (i < j && cmp(arr[mapIndex(j, arr)], pivot) > 0) {
      j -= 1
    }
    while (i < j && cmp(arr[mapIndex(i, arr)], pivot) <= 0) {
      i += 1
    }
    swap(arr, mapIndex(i, arr), mapIndex(j, arr))
  }

  swap(arr, mapIndex(i, arr), mapIndex(left, arr))
  return i
}

function swap(arr: any[], i: number, j: number) {
  [arr[i], arr[j]] = [arr[j], arr[i]]
}
// @lc code=end
