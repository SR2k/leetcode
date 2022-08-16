/*
 * @lc app=leetcode.cn id=215 lang=typescript
 *
 * [215] 数组中的第K个最大元素
 *
 * https://leetcode.cn/problems/kth-largest-element-in-an-array/description/
 *
 * algorithms
 * Medium (64.74%)
 * Likes:    1714
 * Dislikes: 0
 * Total Accepted:    660K
 * Total Submissions: 1M
 * Testcase Example:  '[3,2,1,5,6,4]\n2'
 *
 * 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
 *
 * 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: [3,2,1,5,6,4] 和 k = 2
 * 输出: 5
 *
 *
 * 示例 2:
 *
 *
 * 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
 * 输出: 4
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * -10^4
 *
 *
 */

export
// @lc code=start
function findKthLargest(nums: number[], k: number): number {
  quickSelect(nums, (a, b) => a - b, k)
  return nums[nums.length - k]
}

type CompareFunc<T> = (a: T, b: T) => number

function quickSelect<T>(
  arr: T[],
  compare: CompareFunc<T>,
  topK: number,
  left = 0,
  right = arr.length - 1,
) {
  if (left >= right) return

  const i = partition(arr, compare, left, right)
  const target = right - topK + 1

  if (i < target) {
    quickSelect(arr, compare, topK, i + 1, right)
  } else if (i > target) {
    quickSelect(arr, compare, i - target, left, i - 1)
  }
}

function partition<T>(
  arr: T[],
  compare: CompareFunc<T>,
  left: number,
  right: number,
) {
  const randomIndex = Math.floor(Math.random() * (right - left) + left)
  swap(arr, randomIndex, left)

  const pivotValue = arr[left]
  let i = left, j = right
  while (i < j) {
    while (i < j && compare(arr[j], pivotValue) > 0) {
      j--
    }
    while (i < j && compare(arr[i], pivotValue) <= 0) {
      i++
    }
    swap(arr, i, j)
  }

  swap(arr, i, left)
  return i
}

function swap(arr: any[], i: number, j: number) {
  const temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}
// @lc code=end
