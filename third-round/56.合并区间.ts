/*
 * @lc app=leetcode.cn id=56 lang=typescript
 *
 * [56] 合并区间
 *
 * https://leetcode-cn.com/problems/merge-intervals/description/
 *
 * algorithms
 * Medium (47.85%)
 * Likes:    1304
 * Dislikes: 0
 * Total Accepted:    365.7K
 * Total Submissions: 764.2K
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
function merge(intervals: [number, number][]): [number, number][] {
  intervals.sort((a, b) => a[0] - b[0])
  const result: [number, number][] = []

  for (const [begin, end] of intervals) {
    const [prevBegin, prevEnd] = result.length ? result[result.length - 1] : [-Infinity, -Infinity]

    if (result.length && begin >= prevBegin && begin <= prevEnd) {
      result[result.length - 1][1] = Math.max(prevEnd, end)
    } else {
      result.push([begin, end])
    }
  }

  return result
}
// @lc code=end
