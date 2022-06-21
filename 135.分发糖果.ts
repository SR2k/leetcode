/*
 * @lc app=leetcode.cn id=135 lang=typescript
 *
 * [135] 分发糖果
 *
 * https://leetcode.cn/problems/candy/description/
 *
 * algorithms
 * Hard (49.18%)
 * Likes:    887
 * Dislikes: 0
 * Total Accepted:    150K
 * Total Submissions: 304.7K
 * Testcase Example:  '[1,0,2]'
 *
 * n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
 *
 * 你需要按照以下要求，给这些孩子分发糖果：
 *
 *
 * 每个孩子至少分配到 1 个糖果。
 * 相邻两个孩子评分更高的孩子会获得更多的糖果。
 *
 *
 * 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：ratings = [1,0,2]
 * 输出：5
 * 解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
 *
 *
 * 示例 2：
 *
 *
 * 输入：ratings = [1,2,2]
 * 输出：4
 * 解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
 * ⁠    第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
 *
 *
 *
 * 提示：
 *
 *
 * n == ratings.length
 * 1 <= n <= 2 * 10^4
 * 0 <= ratings[i] <= 2 * 10^4
 *
 *
 */

export
// @lc code=start
function candy(ratings: number[]): number {
  const left: number[] = []
  ratings.forEach((r, i) => {
    if (i > 0 && r > ratings[i - 1]) {
      left.push(left[i - 1] + 1)
    } else {
      left.push(1)
    }
  })

  let result = 0
  let prev = 0
  for (let i = ratings.length - 1; i >= 0; i--) {
    let right = 1
    if (i < ratings.length - 1 && ratings[i] > ratings[i + 1]) {
      right = prev + 1
    }
    prev = right
    result += Math.max(left[i], prev)
  }

  return result
}
// @lc code=end
