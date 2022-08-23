/*
 * @lc app=leetcode.cn id=347 lang=typescript
 *
 * [347] 前 K 个高频元素
 *
 * https://leetcode.cn/problems/top-k-frequent-elements/description/
 *
 * algorithms
 * Medium (63.23%)
 * Likes:    1292
 * Dislikes: 0
 * Total Accepted:    337.9K
 * Total Submissions: 534.1K
 * Testcase Example:  '[1,1,1,2,2,3]\n2'
 *
 * 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: nums = [1,1,1,2,2,3], k = 2
 * 输出: [1,2]
 *
 *
 * 示例 2:
 *
 *
 * 输入: nums = [1], k = 1
 * 输出: [1]
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * k 的取值范围是 [1, 数组中不相同的元素的个数]
 * 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
 *
 *
 *
 *
 * 进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
 *
 */

export
// @lc code=start
function topKFrequent(nums: number[], k: number): number[] {
  const freq: Record<number, number> = {}
  const numSet = new Set<number>()

  nums.forEach((n) => {
    freq[n] = 1 + (freq[n] || 0)
    numSet.add(n)
  })

  nums = [...numSet]

  quickSelect(
    nums,
    (a, b) => freq[a] - freq[b],
    0,
    nums.length - 1,
    k,
  )
  return nums.slice(-k)
}

function quickSelect<T>(
  nums: T[],
  compare: (a: T, b: T) => number,
  left: number,
  right: number,
  k: number,
) {
  if (left >= right) return

  const i = partition(nums, compare, left, right)
  const target = right - k + 1

  if (i > target) {
    quickSelect(nums, compare, left, i - 1, i - target)
  } else if (i < target) {
    quickSelect(nums, compare, i + 1, right, k)
  }
}

function partition<T>(
  nums: T[],
  compare: (a: T, b: T) => number,
  left: number,
  right: number,
) {
  const random = Math.floor(Math.random() * (right - left) + left)
  swap(nums, left, random)

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
// @lc code=end
