/*
 * @lc app=leetcode.cn id=117 lang=typescript
 *
 * [117] 填充每个节点的下一个右侧节点指针 II
 *
 * https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/description/
 *
 * algorithms
 * Medium (62.63%)
 * Likes:    506
 * Dislikes: 0
 * Total Accepted:    110.3K
 * Total Submissions: 176.2K
 * Testcase Example:  '[1,2,3,4,5,null,7]'
 *
 * 给定一个二叉树
 *
 *
 * struct Node {
 * ⁠ int val;
 * ⁠ Node *left;
 * ⁠ Node *right;
 * ⁠ Node *next;
 * }
 *
 * 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
 *
 * 初始状态下，所有 next 指针都被设置为 NULL。
 *
 *
 *
 * 进阶：
 *
 *
 * 你只能使用常量级额外空间。
 * 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 *
 *
 *
 *
 * 示例：
 *
 *
 *
 *
 * 输入：root = [1,2,3,4,5,null,7]
 * 输出：[1,#,2,3,#,4,5,7,#]
 * 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next
 * 指针连接），'#' 表示每层的末尾。
 *
 *
 *
 * 提示：
 *
 *
 * 树中的节点数小于 6000
 * -100
 *
 *
 *
 *
 *
 *
 *
 */

import { TreeNode } from './commons/Tree'

export class Node<T = any> extends TreeNode<T> {
  constructor(
    public val: T,
    public left: Node<T> | null = null,
    public right: Node<T> | null = null,
    public next: Node<T> | null = null,
  ) {
    super(val, left, right)
  }

  toString() {
    let entry: Node<T> | null = this
    const result: Array<T | '#'> = []

    while (entry) {
      let nextEntry: Node<T> | null = null
      let curr: Node<T> | null = entry

      while (curr) {
        nextEntry = nextEntry || curr.left || curr.right
        result.push(curr.val)
        curr = curr.next
      }

      entry = nextEntry
      result.push('#')
    }

    return result.join(',')
  }
}

export
// @lc code=start
function connect(root: Node | null): Node | null {
  let nextChildEntry: Node | null = root
  let currParent: Node | null = null

  while (nextChildEntry) {
    currParent = nextChildEntry
    nextChildEntry = null
    let prev = null

    while (currParent) {
      if (currParent.left) {
        prev = linkAndMove(prev, currParent.left)
      }
      if (currParent.right) {
        prev = linkAndMove(prev, currParent.right)
      }
      nextChildEntry = nextChildEntry || currParent.left || currParent.right
      currParent = currParent.next
    }
  }

  return root
}

function linkAndMove(prev: Node | null, next: Node) {
  if (!prev) return next
  prev.next = next
  return next
}
// @lc code=end
