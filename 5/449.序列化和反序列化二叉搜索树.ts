/*
 * @lc app=leetcode.cn id=449 lang=typescript
 *
 * [449] 序列化和反序列化二叉搜索树
 *
 * https://leetcode.cn/problems/serialize-and-deserialize-bst/description/
 *
 * algorithms
 * Medium (60.55%)
 * Likes:    362
 * Dislikes: 0
 * Total Accepted:    42.8K
 * Total Submissions: 70.8K
 * Testcase Example:  '[2,1,3]'
 *
 * 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
 *
 * 设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。
 * 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
 *
 * 编码的字符串应尽可能紧凑。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [2,1,3]
 * 输出：[2,1,3]
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = []
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点数范围是 [0, 10^4]
 * 0 <= Node.val <= 10^4
 * 题目数据 保证 输入的树是一棵二叉搜索树。
 *
 *
 */

import { TreeNode } from './commons/Tree'

// @lc code=start
/*
 * Encodes a tree to a single string.
 */
function serialize(root: TreeNode | null): string {
  return postorder(root).join(',')
}

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
  if (!data) return null

  const values = data.split(',').map((x) => +x)

  function buildTree(min: number, max: number): TreeNode|null {
    if (!values.length) return null
    const value = values[values.length - 1]
    if (value < min || value > max) return null

    const root = new TreeNode(values.pop()!)
    root.right = buildTree(Math.max(min, value), max)
    root.left = buildTree(min, Math.min(max, value))

    return root
  }

  return buildTree(Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER)
}

function postorder(node: TreeNode | null, result: number[] = []): number[] {
  if (!node) return result

  postorder(node.left, result)
  postorder(node.right, result)
  result.push(node.val)

  return result
}
// @lc code=end

[2,1,3]

       5
   3       7
 2   4  6    8

[2,4,3,6,8,7,5]

// [7, inf]
// 
// 
