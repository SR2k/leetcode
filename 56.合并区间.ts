/*
 * @lc app=leetcode.cn id=56 lang=typescript
 *
 * [56] 合并区间
 *
 * https://leetcode.cn/problems/merge-intervals/description/
 *
 * algorithms
 * Medium (49.02%)
 * Likes:    1606
 * Dislikes: 0
 * Total Accepted:    508.2K
 * Total Submissions: 1M
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
  quickSort(
    intervals,
    (a, b) => {
      if (a[0] !== b[0]) {
        return a[0] - b[0]
      }
      return a[1] - b[1]
    },
  )

  const result: Array<[number, number]> = []

  for (const [begin, end] of intervals) {
    const prevEnd = result[result.length - 1]?.[1] ?? Number.MIN_SAFE_INTEGER

    if (prevEnd < begin) {
      result.push([begin, end])
    } else {
      result[result.length - 1][1] = Math.max(prevEnd, end)
    }
  }

  return result
}

function quickSort<T>(
  arr: T[],
  compare: (a: T, b: T) => number,
  left = 0,
  right = arr.length - 1,
) {
  if (right <= left) return

  const i = partition(arr, compare, left, right)
  quickSort(arr, compare, left, i - 1)
  quickSort(arr, compare, i + 1, right)
}

function partition<T>(
  arr: T[],
  compare: (a: T, b: T) => number,
  left: number,
  right: number,
): number {
  const pivotValue = arr[left]
  let j = left
  for (let i = left + 1; i <= right; i++) {
    if (compare(arr[i], pivotValue) <= 0) {
      swap(arr, i, ++j)
    }
  }

  swap(arr, left, j)
  return j
}

function swap(arr: any[], i: number, j: number) {
  const temp = arr[j]
  arr[j] = arr[i]
  arr[i] = temp
}
// @lc code=end
