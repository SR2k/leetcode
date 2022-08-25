/*
 * @lc app=leetcode.cn id=836 lang=typescript
 *
 * [836] 矩形重叠
 *
 * https://leetcode.cn/problems/rectangle-overlap/description/
 *
 * algorithms
 * Easy (48.67%)
 * Likes:    259
 * Dislikes: 0
 * Total Accepted:    45.2K
 * Total Submissions: 92.8K
 * Testcase Example:  '[0,0,2,2]\n[1,1,3,3]'
 *
 * 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。矩形的上下边平行于
 * x 轴，左右边平行于 y 轴。
 *
 * 如果相交的面积为 正 ，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
 *
 * 给出两个矩形 rec1 和 rec2 。如果它们重叠，返回 true；否则，返回 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
 * 输出：false
 *
 *
 * 示例 3：
 *
 *
 * 输入：rec1 = [0,0,1,1], rec2 = [2,2,3,3]
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * rect1.length == 4
 * rect2.length == 4
 * -10^9 <= rec1[i], rec2[i] <= 10^9
 * rec1 和 rec2 表示一个面积不为零的有效矩形
 *
 *
 */

export
// @lc code=start
function isRectangleOverlap(rec1: number[], rec2: number[]): boolean {
  const [xa1, ya1, xa2, ya2] = rec1
  const [xb1, yb1, xb2, yb2] = rec2
  const overlapX = Math.min(xa2, xb2) - Math.max(xa1, xb1)
  const overlapY = Math.min(ya2, yb2) - Math.max(ya1, yb1)
  return overlapX > 0 && overlapY > 0
}
// @lc code=end
