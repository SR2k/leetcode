/*
 * @lc app=leetcode.cn id=700 lang=typescript
 *
 * [700] 二叉搜索树中的搜索
 *
 * https://leetcode.cn/problems/search-in-a-binary-search-tree/description/
 *
 * algorithms
 * Easy (77.45%)
 * Likes:    280
 * Dislikes: 0
 * Total Accepted:    171.2K
 * Total Submissions: 221K
 * Testcase Example:  '[4,2,7,1,3]\n2'
 *
 * 给定二叉搜索树（BST）的根节点 root 和一个整数值 val。
 *
 * 你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。
 *
 *
 *
 * 示例 1:
 *
 *
 *
 *
 * 输入：root = [4,2,7,1,3], val = 2
 * 输出：[2,1,3]
 *
 *
 * Example 2:
 *
 *
 * 输入：root = [4,2,7,1,3], val = 5
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 数中节点数在 [1, 5000] 范围内
 * 1 <= Node.val <= 10^7
 * root 是二叉搜索树
 * 1 <= val <= 10^7
 *
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function searchBST(root: TreeNode | null, val: number): TreeNode | null {
  let curr = root

  while (curr) {
    if (val === curr.val) {
      break
    }

    if (val < curr.val) {
      curr = curr.left
    } else {
      curr = curr.right
    }
  }

  return curr
}
// @lc code=end
