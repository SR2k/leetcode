/*
 * @lc app=leetcode.cn id=968 lang=typescript
 *
 * [968] 监控二叉树
 *
 * https://leetcode.cn/problems/binary-tree-cameras/description/
 *
 * algorithms
 * Hard (51.35%)
 * Likes:    413
 * Dislikes: 0
 * Total Accepted:    39.1K
 * Total Submissions: 76K
 * Testcase Example:  '[0,0,null,0,0]'
 *
 * 给定一个二叉树，我们在树的节点上安装摄像头。
 *
 * 节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
 *
 * 计算监控树的所有节点所需的最小摄像头数量。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：[0,0,null,0,0]
 * 输出：1
 * 解释：如图所示，一台摄像头足以监控所有节点。
 *
 *
 * 示例 2：
 *
 *
 *
 * 输入：[0,0,null,0,null,0,null,null,0]
 * 输出：2
 * 解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
 *
 *
 *
 * 提示：
 *
 *
 * 给定树的节点数的范围是 [1, 1000]。
 * 每个节点的值都是 0。
 *
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function minCameraCover(root: TreeNode | null): number {
  if (!root) return 0

  function helper(node: TreeNode): DPArray {
    if (!node.left && !node.right) {
      // console.log(node.val, [1, MAX_VAL, 0])
      return [1, MAX_VAL, 0]
    }

    if (!node.left || !node.right) {
      const child = helper(node.left || node.right!)
      // console.log(node.val, [
      //   Math.min(...child) + 1,
      //   child[0],
      //   child[1],
      // ])
      return [
        Math.min(...child) + 1,
        child[0],
        child[1],
      ]
    }

    const left = helper(node.left!), right = helper(node.right!)

    const result: DPArray = [MAX_VAL, MAX_VAL, MAX_VAL]
    result[0] = Math.min(...left) + Math.min(...right) + 1
    result[1] = Math.min(left[0] + right[0], left[1] + right[0], left[0] + right[1])
    result[2] = left[1] + right[1]

    // console.log(node.val, result)

    return result
  }

  const result = helper(root)
  return Math.min(result[0], result[1])
}

type DPArray = [number, number, number]

const MAX_VAL = Infinity
// @lc code=end

console.log(
  minCameraCover(TreeNode.fromArray([1, 2, null, 3, 4, 5, null, null, 6])),
)
