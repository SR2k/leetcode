/*
 * @lc app=leetcode.cn id=179 lang=typescript
 *
 * [179] 最大数
 *
 * https://leetcode.cn/problems/largest-number/description/
 *
 * algorithms
 * Medium (41.16%)
 * Likes:    962
 * Dislikes: 0
 * Total Accepted:    161.8K
 * Total Submissions: 393.1K
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
  sort(nums, (a, b) => cmp(a, b))

  while (nums.length && nums[0] === 0) {
    nums.shift()
  }
  return nums.length ? nums.join('') : '0'
}

function sort<T>(nums: T[], compare: (a: T, b: T) => number, left = 0, right = nums.length - 1) {
  if (left >= right) return

  const i = partition(nums, compare, left, right)

  // console.log(nums, i, nums.slice(left, i), nums[i], nums.slice(i + 1, right + 1))

  sort(nums, compare, left, i - 1)
  sort(nums, compare, i + 1, right)
}

function partition<T>(nums: T[], compare: (a: T, b: T) => number, left: number, right: number) {
  const randomIndex = Math.floor(Math.random() * (right - left) + left)
  swap(nums, randomIndex, left)

  const pivotValue = nums[left]
  let j = left
  for (let i = left + 1; i <= right; i++) {
    if (compare(nums[i], pivotValue) <= 0) {
      swap(nums, ++j, i)
    }
  }

  swap(nums, left, j)
  return j
}

function swap(arr: any[], i: number, j: number) {
  const temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}

function cmp(a: string | number, b: string | number) {
  const ab = String(a) + String(b), ba = String(b) + String(a)
  for (let i = 0; i < ab.length; i++) {
    if (ab[i] < ba[i]) {
      return 1
    } else if (ab[i] > ba[i]) {
      return -1
    }
  }
  return 0
}
// @lc code=end

const arr = [5, 6, 8, 3, 2, 9, 0, 1]
sort(arr, (a, b) => a - b)
console.log(arr)
