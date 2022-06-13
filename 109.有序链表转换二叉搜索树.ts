/*
 * @lc app=leetcode.cn id=109 lang=typescript
 *
 * [109] 有序链表转换二叉搜索树
 *
 * https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/description/
 *
 * algorithms
 * Medium (76.27%)
 * Likes:    712
 * Dislikes: 0
 * Total Accepted:    120.2K
 * Total Submissions: 157.6K
 * Testcase Example:  '[-10,-3,0,5,9]'
 *
 * 给定一个单链表的头节点  head ，其中的元素 按升序排序 ，将其转换为高度平衡的二叉搜索树。
 *
 * 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差不超过 1。
 *
 *
 *
 * 示例 1:
 *
 *
 *
 *
 * 输入: head = [-10,-3,0,5,9]
 * 输出: [0,-3,9,-10,null,5]
 * 解释: 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。
 *
 *
 * 示例 2:
 *
 *
 * 输入: head = []
 * 输出: []
 *
 *
 *
 *
 * 提示:
 *
 *
 * head 中的节点数在[0, 2 * 10^4] 范围内
 * -10^5 <= Node.val <= 10^5
 *
 *
 */

import { TreeNode } from './commons/Tree'
import { ListNode } from './commons/list'

export
// @lc code=start
function sortedListToBST(head: ListNode | null): TreeNode | null {
  const length = lengthOfList(head)
  if (!length) return null

  const result = buildTree(length)
  fillTree(result, head)
  return result
}

const lengthOfList = (head: ListNode | null) => {
  let result = 0

  while (head) {
    result += 1
    head = head.next
  }

  return result
}

const buildTree = (size: number): TreeNode | null => {
  if (size === 0) {
    return null
  }

  const leftSize = Math.floor((size - 1) / 2)
  const rightSize = size - 1 - leftSize
  const node = new TreeNode(-1, buildTree(leftSize), buildTree(rightSize))
  return node
}

const fillTree = (root?: TreeNode | null, list?: ListNode | null): ListNode | null | undefined => {
  if (!root || !list) return list

  list = fillTree(root.left, list)
  root.val = list?.val
  list = list?.next
  list = fillTree(root.right, list)

  return list
}
// @lc code=end

// [0,-10,5,null,-3,null,9]
//             0
//      -10          5
//   x    -3    x       9
