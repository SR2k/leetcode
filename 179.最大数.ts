/*
 * @lc app=leetcode.cn id=179 lang=typescript
 *
 * [179] 最大数
 *
 * https://leetcode.cn/problems/largest-number/description/
 *
 * algorithms
 * Medium (41.19%)
 * Likes:    994
 * Dislikes: 0
 * Total Accepted:    171K
 * Total Submissions: 415.3K
 * Testcase Example:  '[10,2]'
 *
 * 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
 *
 * 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [10,2]
 * 输出："210"
 *
 * 示例 2：
 *
 *
 * 输入：nums = [3,30,34,5,9]
 * 输出："9534330"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 100
 * 0 <= nums[i] <= 10^9
 *
 *
 */

export
// @lc code=start
function largestNumber(nums: number[]): string {
  quickSort(
    nums,
    (a, b) => {
      const x = `${a}${b}`, y = `${b}${a}`
      for (let i = 0; i < x.length; i++) {
        if (x[i] > y[i]) {
          return 1
        } else if (x[i] < y[i]) {
          return -1
        }
      }
      return 0
    },
  )

  while (nums.length && nums.at(-1) === 0) {
    nums.pop()
  }

  nums.reverse()
  return nums.join('') || '0'
}

function swap(arr: any[], i: number, j: number) {
  const temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}

function partition<T>(arr: T[], compare: (a: T, b: T) => number, left: number, right: number) {
  const random = Math.floor(Math.random() * (right - left)) + left
  swap(arr, left, random)

  const pivotValue = arr[left]
  let j = left
  for (let i = left + 1; i <= right; i++) {
    if (compare(arr[i], pivotValue) <= 0) {
      swap(arr, ++j, i)
    }
  }

  swap(arr, left, j)
  return j
}

function quickSort<T>(
  arr: T[],
  compare: (a: T, b: T) => number,
  left = 0,
  right = arr.length - 1,
) {
  if (left >= right) return

  const i = partition(arr, compare, left, right)
  quickSort(arr, compare, left, i - 1)
  quickSort(arr, compare, i + 1, right)
}
// @lc code=end
