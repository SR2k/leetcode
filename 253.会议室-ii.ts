/*
 * @lc app=leetcode.cn id=253 lang=typescript
 *
 * [253] 会议室 II
 *
 * https://leetcode-cn.com/problems/meeting-rooms-ii/description/
 *
 * algorithms
 * Medium (50.81%)
 * Likes:    391
 * Dislikes: 0
 * Total Accepted:    39.1K
 * Total Submissions: 77K
 * Testcase Example:  '[[0,30],[5,10],[15,20]]'
 *
 * 给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi]
 * ，返回 所需会议室的最小数量 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：intervals = [[0,30],[5,10],[15,20]]
 * 输出：2
 *
 *
 * 示例 2：
 *
 *
 * 输入：intervals = [[7,10],[2,4]]
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= intervals.length <= 10^4
 * 0 <= starti < endi <= 10^6
 *
 *
 */

export
// @lc code=start
function minMeetingRooms(intervals: number[][]): number {
  const delta: Array<[number, number]> = []
  for (const [begin, end] of intervals) {
    delta.push([1, begin])
    delta.push([-1, end])
  }
  delta.sort((a, b) => {
    if (a[1] !== b[1]) {
      return a[1] - b[1]
    }

    return a[0] - b[0]
  })
  let curr = 0; let
    result = 0
  for (const [d] of delta) {
    curr += d
    result = Math.max(curr, result)
  }
  return result
}
// @lc code=end
