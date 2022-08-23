/*
 * @lc app=leetcode.cn id=297 lang=typescript
 *
 * [297] 二叉树的序列化与反序列化
 *
 * https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/description/
 *
 * algorithms
 * Hard (58.25%)
 * Likes:    952
 * Dislikes: 0
 * Total Accepted:    178K
 * Total Submissions: 305.6K
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

export
// @lc code=start
function serialize(root: TreeNode | null): string {
  const queue: Array<TreeNode | null> = [root]

  const resultQueue: Array<string> = []
  let nullCount = 0
  while (queue.length) {
    const node = queue.shift()
    if (!node) {
      nullCount++
      continue
    }

    if (nullCount) {
      for (let i = 0; i < nullCount; i++) {
        resultQueue.push('#')
      }
      nullCount = 0
    }

    resultQueue.push(String(node.val))
    queue.push(node.left)
    queue.push(node.right)
  }

  return resultQueue.join(',') || '#'
}

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
  const values = data
    .split(',')
    .map((x) => (x === '#' ? null : parseInt(x, 10)))

  if (!values.length) {
    return null
  }

  const rootValue = values.shift()
  if (rootValue === null) return null

  const root = new TreeNode(rootValue)
  const nodeQueue = [root]

  while (values.length) {
    const node = nodeQueue.shift()!

    const leftValue = values.shift()
    if (leftValue !== null) {
      node.left = new TreeNode(leftValue)
      nodeQueue.push(node.left)
    }

    if (!values.length) break

    const rightValue = values.shift()
    if (rightValue !== null) {
      node.right = new TreeNode(rightValue)
      nodeQueue.push(node.right)
    }
  }

  return root
}
// @lc code=end
