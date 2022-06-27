/*
 * @lc app=leetcode.cn id=179 lang=typescript
 *
 * [179] 最大数
 *
 * https://leetcode.cn/problems/largest-number/description/
 *
 * algorithms
 * Medium (41.16%)
 * Likes:    936
 * Dislikes: 0
 * Total Accepted:    155.9K
 * Total Submissions: 378.7K
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

// @lc code=start
function largestNumber(nums: number[]): string {
  quickSort(nums, (a, b) => Number(`${b}${a}`) - Number(`${a}${b}`))

  let result = ''
  for (const n of nums) {
    if (n !== 0 || result) {
      result += String(n)
    }
  }

  return result || '0'
}

function quickSort<T>(arr: T[], cmp: (a: T, b: T) => number, left = 0, right = arr.length - 1) {
  if (left >= right) {
    return
  }

  const i = partition(arr, cmp, left, right)
  quickSort(arr, cmp, left, i - 1)
  quickSort(arr, cmp, i + 1, right)
}

function partition<T>(arr: T[], cmp: (a: T, b: T) => number, left: number, right: number) {
  const rand = Math.floor(Math.random() * (right - left)) + left
  swap(arr, left, rand)

  let i = left, j = right
  while (i < j) {
    while (i < j && cmp(arr[j], arr[left]) > 0) {
      j -= 1
    }
    while (i < j && cmp(arr[i], arr[left]) <= 0) {
      i += 1
    }
    swap(arr, i, j)
  }
  swap(arr, i, left)
  return i
}

function swap(arr: any[], i: number, j: number) {
  const tmp = arr[i]
  arr[i] = arr[j]
  arr[j] = tmp
}
// @lc code=end

console.log(largestNumber([0, 2]))
console.log(largestNumber([0, 0]))
console.log(largestNumber([10, 2]))
console.log(largestNumber([3, 30, 34, 5, 9]))
