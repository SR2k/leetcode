/*
 * @lc app=leetcode.cn id=297 lang=typescript
 *
 * [297] 二叉树的序列化与反序列化
 *
 * https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/description/
 *
 * algorithms
 * Hard (56.54%)
 * Likes:    734
 * Dislikes: 0
 * Total Accepted:    122.2K
 * Total Submissions: 216.1K
 * Testcase Example:  '[1,2,3,null,null,4,5]'
 *
 *
 * 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
 *
 * 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 /
 * 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
 *
 * 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode
 * 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [1,2,3,null,null,4,5]
 * 输出：[1,2,3,null,null,4,5]
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
 * 输入：root = [1]
 * 输出：[1]
 *
 *
 * 示例 4：
 *
 *
 * 输入：root = [1,2]
 * 输出：[1,2]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中结点数在范围 [0, 10^4] 内
 * -1000
 *
 *
 */

import { TreeNode } from './commons/Tree'

// @lc code=start
/*
 * Encodes a tree to a single string.
 */
function serialize(root: TreeNode | null): string {
  const result: Array<number | 'null'> = []
  const queue: Array<TreeNode | null> = [root]

  while (queue.length) {
    const curr = queue.shift()
    result.push(curr?.val ?? 'null')
    if (curr) {
      queue.push(curr.left)
      queue.push(curr.right)
    }
  }

  return result.join(',')
}

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
  const parsed = data.split(',')
    .map((x) => (x === 'null' ? null : +x))

  const headVal = parsed.shift()
  if (headVal === null || headVal === undefined) return null
  const head: TreeNode = new TreeNode(headVal)
  const queue: TreeNode[] = [head]

  while (parsed.length) {
    const node = queue.shift()
    const leftVal = parsed.shift()
    const rightVal = parsed.shift()

    if (leftVal !== null && leftVal !== undefined) {
      const left = new TreeNode(leftVal)
      if (node) node.left = left
      queue.push(left)
    }
    if (rightVal !== null && rightVal !== undefined) {
      const right = new TreeNode(rightVal)
      if (node) node.right = right
      queue.push(right)
    }
  }

  return head
}

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
// @lc code=end

export const s = serialize
export const d = deserialize
