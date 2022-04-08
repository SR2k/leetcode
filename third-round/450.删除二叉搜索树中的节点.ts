/*
 * @lc app=leetcode.cn id=450 lang=typescript
 *
 * [450] 删除二叉搜索树中的节点
 *
 * https://leetcode-cn.com/problems/delete-node-in-a-bst/description/
 *
 * algorithms
 * Medium (49.65%)
 * Likes:    642
 * Dislikes: 0
 * Total Accepted:    82.9K
 * Total Submissions: 166.8K
 * Testcase Example:  '[5,3,6,2,4,null,7]\n3'
 *
 * 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key
 * 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
 *
 * 一般来说，删除节点可分为两个步骤：
 *
 *
 * 首先找到需要删除的节点；
 * 如果找到了，删除它。
 *
 *
 *
 *
 * 示例 1:
 *
 *
 *
 *
 * 输入：root = [5,3,6,2,4,null,7], key = 3
 * 输出：[5,4,6,2,null,null,7]
 * 解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
 * 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
 * 另一个正确答案是 [5,2,6,null,4,null,7]。
 *
 *
 *
 *
 * 示例 2:
 *
 *
 * 输入: root = [5,3,6,2,4,null,7], key = 0
 * 输出: [5,3,6,2,4,null,7]
 * 解释: 二叉树不包含值为 0 的节点
 *
 *
 * 示例 3:
 *
 *
 * 输入: root = [], key = 0
 * 输出: []
 *
 *
 *
 * 提示:
 *
 *
 * 节点数的范围 [0, 10^4].
 * -10^5 <= Node.val <= 10^5
 * 节点值唯一
 * root 是合法的二叉搜索树
 * -10^5 <= key <= 10^5
 *
 *
 *
 *
 * 进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
  if (!root) return root

  if (root.val > key) {
    root.left = deleteNode(root.left, key)
    return root
  }
  if (root.val < key) {
    root.right = deleteNode(root.right, key)
    return root
  }
  if (!root.left || !root.right) {
    return root.left || root.right
  }

  const [sucParent, suc] = findSuccessor(root)
  root.val = suc.val
  if (sucParent.left === suc) {
    sucParent.left = deleteNode(suc, suc.val)
  } else {
    sucParent.right = deleteNode(suc, suc.val)
  }

  return root
}

function findSuccessor(node: TreeNode) {
  let parent = node
  let curr = node.right!

  while (curr.left) {
    parent = curr
    curr = curr.left
  }

  return [parent, curr]
}

// function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
//   if (!root) return null
//   if (root?.val === key) {
//     return deleteNode(new TreeNode(2e5, root), key)!.left
//   }
//
//   const [parent, node] = findNodeInBST(root, key)
//   if (!node) return root
//
//   if (parent!.left === node) {
//     if (!node.right || !node.left) {
//       parent!.left = node.left || node.right
//       return root
//     }
//     const left = node.left
//     const right = node.right
//     parent!.left = right
//     findEnd(right, 'left').left = left
//   } else {
//     if (!node.right || !node.left) {
//       parent!.right = node.left || node.right
//       return root
//     }
//     const left = node.left
//     const right = node.right
//     parent!.right = left
//     findEnd(left, 'right').right = right
//   }
//
//   return root
// }

// function findNodeInBST(root: TreeNode | null, value: number) {
//   let prevNode = null
//   let currNode = root
//
//   while (currNode) {
//     if (currNode.val === value) {
//       return [prevNode, currNode]
//     }
//     if (currNode.val > value) {
//       prevNode = currNode
//       currNode = currNode.left
//     } else {
//       prevNode = currNode
//       currNode = currNode.right
//     }
//   }
//
//   return []
// }

// function findEnd(node: TreeNode, key: 'left' | 'right') {
//   let curr = node
//   while (curr[key]) {
//     curr = curr[key]!
//   }
//   return curr
// }
// @lc code=end
