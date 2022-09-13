/*
 * @lc app=leetcode.cn id=149 lang=typescript
 *
 * [149] 直线上最多的点数
 *
 * https://leetcode.cn/problems/max-points-on-a-line/description/
 *
 * algorithms
 * Hard (38.01%)
 * Likes:    436
 * Dislikes: 0
 * Total Accepted:    69.1K
 * Total Submissions: 181.3K
 * Testcase Example:  '[[1,1],[2,2],[3,3]]'
 *
 * 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：points = [[1,1],[2,2],[3,3]]
 * 输出：3
 *
 *
 * 示例 2：
 *
 *
 * 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
 * 输出：4
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * points[i].length == 2
 * -10^4 i, yi
 * points 中的所有点 互不相同
 *
 *
 */

export
// @lc code=start
function maxPoints(points: Point[]): number {
  const lines: Record<string, Set<string>> = {}

  for (let i = 0; i < points.length - 1; i++) {
    const p1 = points[i]

    for (let j = i + 1; j < points.length; j++) {
      const p2 = points[j]
      const hash = getLineHash(p1, p2)

      if (!lines[hash]) {
        lines[hash] = new Set<string>()
      }
      lines[hash].add(p1.join(','))
      lines[hash].add(p2.join(','))
    }
  }

  const retLines = Object.values(lines)
  if (!retLines.length) {
    return points.length
  }
  return Math.max(...retLines.map((x) => x.size))
}

type Point = [number, number]

function getLineHash(p1: Point, p2: Point): string {
  const [x1, y1] = p1
  const [x2, y2] = p2

  const dy = y2 - y1, dx = x2 - x1
  if (dx === 0) {
    return String(x1)
  }

  const k = dy / dx
  const b = y1 - k * x1
  return [k, b].join('@')
}
// @lc code=end
