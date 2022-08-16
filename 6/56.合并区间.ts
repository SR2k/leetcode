/*
 * @lc app=leetcode.cn id=56 lang=typescript
 *
 * [56] 合并区间
 *
 * https://leetcode.cn/problems/merge-intervals/description/
 *
 * algorithms
 * Medium (48.68%)
 * Likes:    1531
 * Dislikes: 0
 * Total Accepted:    470.4K
 * Total Submissions: 964.9K
 * Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
 *
 * 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
 * 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
 * 输出：[[1,6],[8,10],[15,18]]
 * 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
 *
 *
 * 示例 2：
 *
 *
 * 输入：intervals = [[1,4],[4,5]]
 * 输出：[[1,5]]
 * 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= intervals.length <= 10^4
 * intervals[i].length == 2
 * 0 <= starti <= endi <= 10^4
 *
 *
 */

export
// @lc code=start
function merge(intervals: number[][]): number[][] {
  quickSort(intervals, (a, b) => a[0] - b[0])
  const result: number[][] = []

  for (const interval of intervals) {
    const [begin, end] = interval

    const prev = result.length
      ? result[result.length - 1]
      : DUMMY_INTERVAL

    if (begin <= prev[1]) {
      prev[1] = Math.max(end, prev[1])
    } else {
      result.push([begin, end])
    }
  }

  return result
}

const DUMMY_INTERVAL = [Number.MIN_SAFE_INTEGER, Number.MIN_SAFE_INTEGER]

type CompareFunc<T> = (a: T, b: T) => number

function quickSort<T>(
  arr: T[],
  compare: CompareFunc<T>,
  left = 0,
  right = arr.length - 1,
) {
  if (left >= right) return

  const i = partition(arr, compare, left, right)
  quickSort(arr, compare, left, i - 1)
  quickSort(arr, compare, i + 1, right)
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

  swap(arr, left, i)
  return i
}

function swap(arr: any[], i: number, j: number) {
  const temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}
// @lc code=end
