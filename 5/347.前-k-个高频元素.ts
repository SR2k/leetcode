/*
 * @lc app=leetcode.cn id=347 lang=typescript
 *
 * [347] 前 K 个高频元素
 *
 * https://leetcode.cn/problems/top-k-frequent-elements/description/
 *
 * algorithms
 * Medium (62.99%)
 * Likes:    1195
 * Dislikes: 0
 * Total Accepted:    296.3K
 * Total Submissions: 470.4K
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
  const counter = new Map<number, number>()
  nums.forEach((n) => {
    counter.set(n, 1 + (counter.get(n) || 0))
  })

  const values = [...counter.keys()]
  return topK(values, k, (a, b) => (counter.get(a)! - counter.get(b)!))
}

const topK = (nums: number[], k: number, cmp: (a: number, b: number) => number) => {
  quickSelect(nums, k, 0, nums.length - 1, cmp)
  return nums.slice(-k)
}

const quickSelect = (nums: number[], k: number, left: number, right: number, cmp: (a: number, b: number) => number) => {
  if (left >= right) return

  const i = partition(nums, left, right, cmp)
  const target = right - k + 1

  if (i < target) {
    quickSelect(nums, k, i + 1, right, cmp)
  } else if (i > target) {
    quickSelect(nums, i - target, left, i - 1, cmp)
  }
}

const partition = (nums: number[], left: number, right: number, cmp: (a: number, b: number) => number) => {
  const randIndex = Math.floor(Math.random() * (right - left)) + left
  swap(nums, left, randIndex)

  const pivotNum = nums[left]
  let i = left, j = right
  while (i < j) {
    while (i < j && cmp(nums[j], pivotNum) > 0) {
      j -= 1
    }
    while (i < j && cmp(nums[i], pivotNum) <= 0) {
      i += 1
    }
    swap(nums, i, j)
  }
  swap(nums, i, left)
  return i
}

const swap = (arr: any[], i: number, j: number) => {
  const tmp = arr[j]
  arr[j] = arr[i]
  arr[i] = tmp
}
// @lc code=end
