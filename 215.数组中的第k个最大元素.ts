/*
 * @lc app=leetcode.cn id=215 lang=typescript
 *
 * [215] 数组中的第K个最大元素
 *
 * https://leetcode.cn/problems/kth-largest-element-in-an-array/description/
 *
 * algorithms
 * Medium (64.65%)
 * Likes:    1821
 * Dislikes: 0
 * Total Accepted:    714.7K
 * Total Submissions: 1.1M
 * Testcase Example:  '[3,2,1,5,6,4]\n2'
 *
 * 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
 *
 * 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
 *
 * 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: [3,2,1,5,6,4], k = 2
 * 输出: 5
 *
 *
 * 示例 2:
 *
 *
 * 输入: [3,2,3,1,2,4,5,5,6], k = 4
 * 输出: 4
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= k <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 *
 *
 */

export
// @lc code=start
function findKthLargest(nums: number[], k: number): number {
  quickSelect(
    nums,
    (a, b) => a - b,
    0,
    nums.length - 1,
    k,
  )

  return nums[nums.length - k]
}

function quickSelect<T>(
  arr: T[],
  compare: (a: T, b: T) => number,
  left: number,
  right: number,
  k: number,
) {
  if (left >= right) return

  const i = partition(arr, compare, left, right)
  const target = right - k + 1

  if (i < target) {
    quickSelect(arr, compare, i + 1, right, k)
  } else if (i > target) {
    quickSelect(arr, compare, left, i - 1, i - target)
  }
}

function partition<T>(
  arr: T[],
  compare: (a: T, b: T) => number,
  left: number,
  right: number,
): number {
  // const randomIndex = Math.floor(Math.random() * (right - left)) + left
  // swap(arr, left, randomIndex)

  const pivotValue = arr[left]

  let j = left
  for (let i = left + 1; i <= right; i++) {
    if (compare(arr[i], pivotValue) <= 0) {
      swap(arr, i, ++j)
    }
  }

  swap(arr, left, j)
  return j
}

function swap(arr: any[], i: number, j: number) {
  const temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}
// @lc code=end
