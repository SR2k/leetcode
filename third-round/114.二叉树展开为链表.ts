/*
 * @lc app=leetcode.cn id=114 lang=typescript
 *
 * [114] 二叉树展开为链表
 *
 * https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
 *
 * algorithms
 * Medium (72.70%)
 * Likes:    1038
 * Dislikes: 0
 * Total Accepted:    207.4K
 * Total Submissions: 285.2K
 * Testcase Example:  '[1,2,5,3,4,null,6]'
 *
 * 给你二叉树的根结点 root ，请你将它展开为一个单链表：
 *
 *
 * 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
 * 展开后的单链表应该与二叉树 先序遍历 顺序相同。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [1,2,5,3,4,null,6]
 * 输出：[1,null,2,null,3,null,4,null,5,null,6]
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = []
 * 输出：[]
 *
 *
 * 示例 3：
 *
 *
 * 输入：root = [0]
 * 输出：[0]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中结点数在范围 [0, 2000] 内
 * -100
 *
 *
 *
 *
 * 进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function flatten(root?: TreeNode | null): void {
  if (!root) return

  if (root.left) {
    if (root.right) {
      const right = root.right
      findPreOfRightChildren(root).right = right
      root.right = root.left
    } else {
      root.right = root.left
    }
    root.left = null
  }

  flatten(root?.right)
}

function findPreOfRightChildren(node: TreeNode) {
  let curr = node.left!

  while (curr.right) {
    curr = curr.right
  }

  return curr
}
// @lc code=end

/**
     1
      \
      2
     /
    3
 */
