/*
 * @lc app=leetcode.cn id=230 lang=typescript
 *
 * [230] 二叉搜索树中第K小的元素
 *
 * https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/
 *
 * algorithms
 * Medium (75.67%)
 * Likes:    667
 * Dislikes: 0
 * Total Accepted:    234.8K
 * Total Submissions: 310.2K
 * Testcase Example:  '[3,1,4,null,2]\n1'
 *
 * 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [3,1,4,null,2], k = 1
 * 输出：1
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [5,3,6,2,4,null,null,1], k = 3
 * 输出：3
 *
 *
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中的节点数为 n 。
 * 1
 * 0
 *
 *
 *
 *
 * 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function kthSmallest(root: TreeNode | null, k: number): number {
  let curr = root
  const stack: TreeNode[] = []

  while (curr || stack.length) {
    while (curr) {
      stack.push(curr)
      curr = curr.left
    }

    curr = stack.pop()!
    if (!--k) return curr.val
    curr = curr.right
  }

  return -1
}
// @lc code=end
