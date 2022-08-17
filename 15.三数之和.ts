/*
 * @lc app=leetcode.cn id=15 lang=typescript
 *
 * [15] 三数之和
 *
 * https://leetcode.cn/problems/3sum/description/
 *
 * algorithms
 * Medium (36.06%)
 * Likes:    5130
 * Dislikes: 0
 * Total Accepted:    1.1M
 * Total Submissions: 3M
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0
 * 且不重复的三元组。
 *
 * 注意：答案中不可以包含重复的三元组。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [-1,0,1,2,-1,-4]
 * 输出：[[-1,-1,2],[-1,0,1]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = []
 * 输出：[]
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [0]
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0
 * -10^5
 *
 *
 */

export
// @lc code=start
function threeSum(nums: number[]): number[][] {
  quickSort(nums, (a, b) => a - b)

  const result: Array<[number, number, number]> = []

  for (let a = 0; a < nums.length - 2; a++) {
    if (a > 0 && nums[a] === nums[a - 1]) {
      continue
    }

    let c = nums.length - 1

    for (let b = a + 1; b < nums.length - 1; b++) {
      if (b > a + 1 && nums[b] === nums[b - 1]) {
        continue
      }

      while (b < c && nums[a] + nums[b] + nums[c] > 0) {
        c--
      }

      if (b >= c) break
      if (nums[a] + nums[b] + nums[c] === 0) {
        result.push([nums[a], nums[b], nums[c]])
      }
    }
  }

  return result
}

function quickSort<T>(
  arr: T[],
  compare: (a: T, b: T) => number,
  begin = 0,
  end = arr.length - 1,
) {
  if (begin >= end) return

  const i = partition(arr, compare, begin, end)
  quickSort(arr, compare, begin, i - 1)
  quickSort(arr, compare, i + 1, end)
}

function partition<T>(
  arr: T[],
  compare: (a: T, b: T) => number,
  begin: number,
  end : number,
): number {
  // todo: rand

  const pivotValue = arr[begin]
  let j = begin
  for (let i = begin + 1; i <= end; i++) {
    if (compare(arr[i], pivotValue) <= 0) {
      swap(arr, i, ++j)
    }
  }

  swap(arr, begin, j)
  return j
}

function swap(arr: any[], i: number, j: number) {
  const temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}
// @lc code=end
