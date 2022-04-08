/*
 * @lc app=leetcode.cn id=101 lang=typescript
 *
 * [101] 对称二叉树
 *
 * https://leetcode-cn.com/problems/symmetric-tree/description/
 *
 * algorithms
 * Easy (57.05%)
 * Likes:    1745
 * Dislikes: 0
 * Total Accepted:    498.1K
 * Total Submissions: 872.9K
 * Testcase Example:  '[1,2,2,3,4,4,3]'
 *
 * 给你一个二叉树的根节点 root ， 检查它是否轴对称。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [1,2,2,3,4,4,3]
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [1,2,2,null,3,null,3]
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点数目在范围 [1, 1000] 内
 * -100 <= Node.val <= 100
 *
 *
 *
 *
 * 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start1
function isSymmetric(root: TreeNode | null): boolean {
  function helper(a: TreeNode | null, b: TreeNode | null): boolean {
    if (!a && !b) return true
    if (!a || !b) return false
    if (a.val !== b.val) return false
    return helper(a.left, b.right) && helper(a.right, b.left)
  }

  return helper(root!.left, root!.right)
}
// @lc code=end
