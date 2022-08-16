/*
 * @lc app=leetcode.cn id=347 lang=typescript
 *
 * [347] 前 K 个高频元素
 *
 * https://leetcode.cn/problems/top-k-frequent-elements/description/
 *
 * algorithms
 * Medium (63.07%)
 * Likes:    1249
 * Dislikes: 0
 * Total Accepted:    312.2K
 * Total Submissions: 494.9K
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
  for (const n of nums) {
    const c = counter.get(n) || 0
    counter.set(n, c + 1)
  }

  const keys = Array.from(counter.keys())
  quickSelect(keys, (a, b) => counter.get(a)! - counter.get(b)!, k)
  return keys.slice(-k)
}

interface CompareFunc<T> {
  (a: T, b: T): number
}

function quickSelect<T>(
  arr: T[],
  compare: CompareFunc<T>,
  k: number,
  left = 0,
  right = arr.length - 1,
) {
  if (left >= right) return

  const i = partition(arr, compare, left, right)
  const target = right - k + 1

  if (i > target) {
    quickSelect(arr, compare, i - target, left, i - 1)
  } else if (i < target) {
    quickSelect(arr, compare, k, i + 1, right)
  }
}

function partition<T>(
  arr: T[],
  compare: CompareFunc<T>,
  left = 0,
  right = arr.length - 1,
) {
  const randomIndex = Math.floor(Math.random() * (right - left) + left)
  swap(arr, randomIndex, left)

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

function swap(arr: any[], i: number, j: number) {
  const temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}
// @lc code=end
