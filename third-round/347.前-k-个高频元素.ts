/*
 * @lc app=leetcode.cn id=347 lang=typescript
 *
 * [347] 前 K 个高频元素
 *
 * https://leetcode-cn.com/problems/top-k-frequent-elements/description/
 *
 * algorithms
 * Medium (62.58%)
 * Likes:    1047
 * Dislikes: 0
 * Total Accepted:    249.6K
 * Total Submissions: 398.8K
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
  const counter: Record<number, number> = {}
  const numSet = new Set<number>()
  for (const n of nums) {
    numSet.add(n)
    counter[n] = (counter[n] || 0) + 1
  }

  const allNums = Array.from(numSet)
  quickSelect(allNums, counter, 0, allNums.length - 1, k)
  return allNums.slice(-k)
}

function quickSelect(nums: number[], by: Record<number, number>, left: number, right: number, k: number) {
  if (left >= right) return

  const i = partition(nums, by, left, right)

  const target = right - k + 1
  if (i < target) {
    quickSelect(nums, by, i + 1, right, k)
  } else if (i > target) {
    quickSelect(nums, by, left, i - 1, k - (right - i + 1))
  }
}

function partition(nums: number[], by: Record<number, number>, left: number, right: number): number {
  const rand = Math.floor(Math.random() * (right - left) + left)
  swap(nums, left, rand)

  const pivot = left
  let i = left, j = right

  while (i < j) {
    while (i < j && by[nums[j]] > by[nums[pivot]]) {
      j--
    }
    while (i < j && by[nums[i]] <= by[nums[pivot]]) {
      i++
    }
    swap(nums, i, j)
  }

  swap(nums, pivot, i)
  return i
}

function swap(nums: number[], i: number, j: number) {
  [nums[i], nums[j]] = [nums[j], nums[i]]
}
// @lc code=end
