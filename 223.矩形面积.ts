/*
 * @lc app=leetcode.cn id=223 lang=typescript
 *
 * [223] 矩形面积
 *
 * https://leetcode.cn/problems/rectangle-area/description/
 *
 * algorithms
 * Medium (53.23%)
 * Likes:    206
 * Dislikes: 0
 * Total Accepted:    51.5K
 * Total Submissions: 96.5K
 * Testcase Example:  '-3\n0\n3\n4\n0\n-1\n9\n2'
 *
 * 给你 二维 平面上两个 由直线构成且边与坐标轴平行/垂直 的矩形，请你计算并返回两个矩形覆盖的总面积。
 *
 * 每个矩形由其 左下 顶点和 右上 顶点坐标表示：
 *
 *
 *
 * 第一个矩形由其左下顶点 (ax1, ay1) 和右上顶点 (ax2, ay2) 定义。
 * 第二个矩形由其左下顶点 (bx1, by1) 和右上顶点 (bx2, by2) 定义。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
 * 输出：45
 *
 *
 * 示例 2：
 *
 *
 * 输入：ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 =
 * 2
 * 输出：16
 *
 *
 *
 *
 * 提示：
 *
 *
 * -10^4 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 10^4
 *
 *
 */

export
// @lc code=start
function computeArea(ax1: number, ay1: number, ax2: number, ay2: number, bx1: number, by1: number, bx2: number, by2: number): number {
  const x = Math.max(Math.min(ax2, bx2) - Math.max(ax1, bx1), 0)
  const y = Math.max(Math.min(ay2, by2) - Math.max(ay1, by1), 0)
  const intersection = x * y
  return (ay2 - ay1) * (ax2 - ax1) + (by2 - by1) * (bx2 - bx1) - intersection
}
// @lc code=end
